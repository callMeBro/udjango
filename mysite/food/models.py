from django.db import models

# Create your models here. 

# produt model for db
class Product(models.Model):
    product_name = models.CharField(max_length=200)
    product_doc = models.CharField(max_length=200)
    product_price = models.IntegerField()
    
    # string representation of an object 
    def __str__(self):
        return self.product_name
    
    
    
    
    
    
    
    