
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .models import Product

def dashboard(request):
    return render(request, "website/dashboard/index.html")
    
def login_view(request):
    # return HttpResponse("Hello world")
    if request.method == "POST":
        email = request.POST["email"]
        password = request.POST["password"]
        
        user = authenticate(request, username=email, password = password)
        # if user is not None:
        #     login(request, user)
        #     messages.success(request, "You have been Logged in Successfully")
        #     return redirect("home")
        # else:
        #     messages.success(request, "There was an error login in")
        #     return redirect("home")
        print("email ", email)
        print("password ", password)
    return render(request, "website/auth/login.html")

def register_view(request):
    # return HttpResponse("Hello world")
    return render(request, "website/auth/register.html")

def home(request):
    # return HttpResponse("Hello world")
    return render(request, "website/home.html")

def productsView(request):
    
    if request.method == "POST":
        pass
    elif request.method == "GET":
        products = Product.objects.all()
        # return HttpResponse("Hello world")
        return render(request, "website/products/products.html", {"products": products})

def singleProductView(request, title):
    # return HttpResponse("Hello world")
    if request.method == "POST":
        pass
    elif request.method == "GET":
        target = Product.objects.get(name= title)
        return render(request, "website/single-product/single-product.html", {"product": product})

def about(request):
    return HttpResponse("Welcome to About us")

def contact(request):
    return HttpResponse("Welcome to Contact us")