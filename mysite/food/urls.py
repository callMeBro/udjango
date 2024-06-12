from . import views
from django.urls import path

# define namespace for urls
app_name='food'

urlpatterns = [
    #/food/
    path("", views.index, name='index'), 
    #/food/id
    path("<int:product_id>", views.info, name='info'), 
    
    path("product/", views.product, name='product'), 
    path('add', views.create_product, name='create_product'),
    # edit 
    path('update/<int:id>/', views.update_product, name='update_product'),
    
    path("delete/<int:id>/", views.delete_product, name='delete_product')
] 