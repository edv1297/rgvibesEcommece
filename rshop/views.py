from django.http import HttpResponse
from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,get_user_model
from .forms import ContactForm,LoginForm,RegisterForm

def home(request):
    context = {
    "title": "Testing out context",

    }
    if request.user.is_authenticated():
        context["premium_content"] = "You are logged in!"
    return render(request, 'home/view.html',context)

def contact(request):
    contact_form = ContactForm(request.POST or None)
    context = {
    "title": "Contact us",
    "message": "Feel free to leave us a message",
    "form": contact_form
    }
    if contact_form.is_valid():
        print(contact_form.cleaned_data)
    return render(request, 'contact/view.html',context)


def login_page(request):
    login_form = LoginForm(request.POST or None)

    context = {
    "title": "Welcome back!",
    "form": login_form
    }

    if login_form.is_valid():
        print(login_form.cleaned_data)
        username = login_form.cleaned_data.get("user_name")
        password = login_form.cleaned_data.get("password")
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            # Redirect to a success page.
            return redirect("/")
        else:
            # Return an 'invalid login' error message.
            redirect("/login")
    return render(request, 'login/index.html', context)

User = get_user_model()
def register_page(request):
    register_form = RegisterForm(request.POST or None)
    context={
    "title": "First, tell us about yourself",
    "form": register_form
    }

    if register_form.is_valid():
        print("Valid Form")
        print(register_form.cleaned_data)
        username = register_form.cleaned_data.get("user_name")
        email = register_form.cleaned_data.get("email")
        password = register_form.cleaned_data.get("password")
        new_user = User.objects.create_user(username,email,password)
        print(new_user)
    return render(request, 'login/register.html', context)

def about(request):
    context = {
    "title": "about"
    }
    return render(request, 'about/view.html',context)

def catalog(request):
    context = {
    "title": "catalog"
    }
    return render(request, 'base.html', context)
