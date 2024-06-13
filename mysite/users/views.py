from django.shortcuts import render, redirect
# from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required 
from .forms import RegisterForm
from django.contrib.auth import logout

# Create your views here.

def register(request):
    if request.method == "POST":                #if request method for the form is post 
        
        
        # form = UserCreationForm(request.POST)
        form = RegisterForm(request.POST)               #save register form post request
        
        if form.is_valid():             #if the form is valid display a message
            form.save()                 #save the user 
            username = form.cleaned_data.get('username')
            messages.success(request, f'Welcome {username}, your account is created' )
            # redirect user to index page
            return redirect('login')
    else:
        # form = UserCreationForm()               #store user creation form in the form 
        form = RegisterForm()                 
        
    return render(request, 'users/register.html', {'form':form})                #


def logout_view(request):
    logout(request)
  
    return render(request, 'users/logout.html')

@login_required
def profilepage(request):
    username = request.user.username
    user = request.user
    context = {'username': username, 'user':user }
    return render(request, 'users/profile.html', context)