from django.http import HttpResponse
from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,get_user_model
from django.utils.http import is_safe_url
from .forms import LoginForm,RegisterForm,GuestForm
from .models import GuestEmail

# Create your views here.

def guest_register_view(request):
    guest_form = GuestForm(request.POST or None)

    context = {
    "form": guest_form
    }

    next_ = request.GET.get('next')
    next_post = request.POST.get('next')
    redirect_path = next_ or next_post or None

    if guest_form.is_valid():
        email = guest_form.cleaned_data.get('email')
        new_guest_email = GuestEmail.objects.create(email=email)
        request.session['guest_email_id'] = new_guest_email.id

        print(is_safe_url(redirect_path, request.get_host()))
        
        if is_safe_url(redirect_path, request.get_host()):
            return redirect(redirect_path)
        else:
            redirect("/")
    return redirect('/register/')

def login_page(request):
    login_form = LoginForm(request.POST or None)

    context = {
    "title": "Welcome back!",
    "form": login_form
    }

    next_ = request.GET.get('next')
    next_post = request.POST.get('next')
    redirect_path = next_ or next_post or None

    if login_form.is_valid():
        username = login_form.cleaned_data.get("user_name")
        password = login_form.cleaned_data.get("password")

        user = authenticate(request, username=username, password=password)

        # If user exists, login the user, else redirect them to login page
        if user is not None:
            login(request, user)
            try:
                del request.session['guest_email_id']
            except:
                pass
            # if the url is safe, redirect user to the next route
            if is_safe_url(redirect_path, request.get_host()):
                return redirect(redirect_path)
            # else:
            #     # return redirect("/")
        else:
            # Return an 'invalid login' error message.
            redirect("/login")
    return render(request, 'accounts/index.html', context)

User = get_user_model()

def register_page(request):
    register_form = RegisterForm(request.POST or None)
    context={
    "title": "First, tell us about yourself",
    "form": register_form
    }

    # Creating a new user if the form is valid
    if register_form.is_valid():
        username = register_form.cleaned_data.get("username")
        email = register_form.cleaned_data.get("email")
        password = register_form.cleaned_data.get("password")
        new_user = User.objects.create_user(username,email,password)
    return render(request, 'accounts/register.html', context)
