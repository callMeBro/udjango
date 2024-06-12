from django import forms 
from .models import Product

# product form class to add items
class ProductForm(forms.ModelForm):             #inherit from the ModelForm 
    class Meta:         #class that holds the fields should be in the form 
        model = Product         #set the model the form will use 
        fields = ['product_name','product_doc','product_price','product_image']
        
        
        