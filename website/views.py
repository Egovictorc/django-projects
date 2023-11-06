
from django.http import HttpResponse
from django.shortcuts import render
from .models import Product

def home(request):
    # return HttpResponse("Hello world")
    return render(request, "website/home.html")

def productsView(request):
    products = Product.objects.all()
    # return HttpResponse("Hello world")
    return render(request, "website/products/products.html", {"products": products})

def singleProductView(request, title):
    # return HttpResponse("Hello world")
    return render(request, "website/single-product/single-product.html", {"title": title})

def about(request):
    return HttpResponse("Welcome to About us")

def contact(request):
    return HttpResponse("Welcome to Contact us")