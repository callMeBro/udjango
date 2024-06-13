from django import forms 
from django.contrib.auth.models import User 
from django.contrib.auth.forms import UserCreationForm

# create register form to inherit from the user creation form
class RegisterForm(UserCreationForm):
    email = forms.EmailField()                  #add additional field 
    
    # define meta class - hold info about register form 
    class Meta:
        model = User
        fields = ['username','email','password1','password2'] 
    