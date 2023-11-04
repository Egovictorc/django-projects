
from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    # return HttpResponse("Hello world")
    return render(request, "website/home.html")

def products(request):
    # return HttpResponse("Hello world")
    return render(request, "website/products/products.html")

def singleProduct(request, title):
    # return HttpResponse("Hello world")
    return render(request, "website/single-product/single-product.html", {"title": title})

def about(request):
    return HttpResponse("Welcome to About us")

def contact(request):
    return HttpResponse("Welcome to Contact us")