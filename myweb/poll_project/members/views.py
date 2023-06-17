from django.shortcuts import render,redirect, get_object_or_404
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from .forms import RegisterUserForm
from django.contrib import messages
from django.contrib.auth.models import User



# Create your views here.











def login_user(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
          login(request, user)
          return redirect('home')
        
        else:
           messages.success(request, ('incorrect username or password, please try again'))
           return redirect('login')
    else:
      return render(request, 'authenticate/login.html', {
        
    })

def logout_user(request):
   logout(request)
   messages.success(request, ("You've logged out..."))
   return redirect('home')

def register_user(request):
    if request.method == "POST":
       form = RegisterUserForm(request.POST)
       if form.is_valid():
          form.save()
          username = form.cleaned_data['username']
          password = form.cleaned_data['password1']
          user = authenticate(username=username, password=password)
          login(request, user)
        #   messages.success(request,"You've registered successfuly!")
          return redirect('home')
    else:
        form = RegisterUserForm()


    return render(request, 'authenticate/register_user.html', {
       'form':form
    })


  
   
    
  



