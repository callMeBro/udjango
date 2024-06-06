from django.shortcuts import render
from django.http import HttpResponse
from .models import Product


# Create your views here.
def hello(request):
    # get objects from database
    productList = Product.objects.all()
    # print("Food Home page.. Hello World")
    return HttpResponse(productList)

# product view
def product(request):
    return HttpResponse('<h1>Product Page</h1>')
    
    