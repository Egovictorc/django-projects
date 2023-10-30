
from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    # return HttpResponse("Hello world")
    return render(request, "home.html")

def about(request):
    return HttpResponse("Welcome to About us")

def contact(request):
    return HttpResponse("Welcome to Contact us")