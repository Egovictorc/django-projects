
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .models import Product

def user_account(request):
    return render(request, "website/dashboard/account.html")

def dashboard(request):
    return render(request, "website/dashboard/index.html")
    
def logout_view(request):
    logout(request)
    messages.success(request, "You have been Logged out Successfully")
    return redirect("website:login")

def login_view(request):
    # return HttpResponse("Hello world")
    if request.method == "POST":
        email = request.POST["email"]
        password = request.POST["password"]
        
        user = authenticate(request, username=email, password = password)
        if user is not None:
            login(request, user)
            messages.success(request, "You have been Logged in Successfully")
            return redirect("website:dashboard")
        else:
            messages.success(request, "There was an error login in")
            # return redirect("dashboard")
        print("email ", email)
        print("password ", password)
    return render(request, "website/auth/login.html")

def register_view(request):
    # return HttpResponse("Hello world")
    if request.method == "POST":
        email = request.POST["email"]
        password = request.POST["password"]
        first_name = request.POST["first_name"]
        last_name = request.POST["last_name"]
        name = ""
        if email and password and first_name and last_name:
            # check if user already exists
            existing_user = User.objects.get(username=email)
            if existing_user:
                messages.success(request, "User already exists, pls sign in")
                return redirect("website:login")
            user = User.objects.create_user(email=email, first_name=first_name, last_name=last_name, password=password,
                                            username=email)
            if user is not None:
                messages.success(request, "Account created successfully")
                return redirect("website/auth/login.html")
            messages.success(request, "Error occured when creating account")
            return render(request, "website/auth/register.html")
        else:
            messages.success(request, "All fields are required")
            return render(request, "website/auth/register.html")

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