from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Product
from django.template import loader 
from .forms import ProductForm


# Create your views here.
def index(request):
    # get objects from database
    productList = Product.objects.all()             #get all products andd save in product list 
    template = loader.get_template('food/index.html')               #lost the home page 
    context = {'productList':productList}               #initialized the context 
    return HttpResponse(template.render(context, request))                            

# product view
def product(request):
    return HttpResponse('<h1>Product Page</h1>')
    
def info(request, product_id):
    product = Product.objects.get(pk=product_id)                #get product based on the id 
    context = {'productList':product}
    return render(request, "food/info.html", context)
    # return HttpResponse("This is produt no/id: %s"  % product_id) 
    
    
    
def create_product(request):
    # get form 
    form = ProductForm(request.POST or None)            #create product form 
    
    if form.is_valid():              #check if the form is valid 
        form.save()             #save the form
        return redirect('food:index')                   #redirect to the homepage 
    return render(request, "food/product-form.html", {"form":form})
    
    
    