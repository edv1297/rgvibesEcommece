from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    context = {
    "title": "Testing out context"
    }
    return render(request, 'base.html',context)

def contact(request):
    context = {
    "title": "contact"
    }
    return render(request, 'base.html',context)

def about(request):
    context = {
    "title": "about"
    }
    return render(request, 'base.html',context)

def catalog(request):
    context = {
    "title": "catalog"
    }
    return render(request, 'base.html', context)
