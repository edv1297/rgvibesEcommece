from django.http import HttpResponse
from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,get_user_model
from .forms import ContactForm

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
