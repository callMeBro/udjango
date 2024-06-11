from django.db import models

# Create your models here. 

# produt model for db
class Product(models.Model):
    product_name = models.CharField(max_length=200)
    product_doc = models.CharField(max_length=200)
    product_price = models.IntegerField()
    product_image = models.CharField(max_length=500, default="https://t4.ftcdn.net/jpg/03/76/40/81/360_F_376408140_kiazgwOvkEy0e50oxgF5kllIl7j2q1SQ.jpg")
    
    
    # string representation of an object 
    def __str__(self):
        return self.product_name
    
    
    
    
    
    
    
    