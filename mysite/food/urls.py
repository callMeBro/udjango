from . import views
from django.urls import path

app_name='food'
urlpatterns = [
    #/food/
    path("", views.index, name='index'), 
    #/food/id
    path("<int:product_id>", views.info, name='info'), 
    
    path("product/", views.product, name='product'), 
    path('add', views.create_product, name='create_product')
] 