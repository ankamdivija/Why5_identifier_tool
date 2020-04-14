from django.shortcuts import render , redirect
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm

from .models import *
from .forms import SignupForm
from .models import UserDetail
from .decorators import unauthenticated_user

# Create your views here.
def home(request):
    if request.user.is_authenticated:
        return redirect('public_dashboard')
    else :
        return render(request,'user/homepage.html',{})


@unauthenticated_user
def Login(request):
    if request.method == 'POST':
        print(request.POST)
        username = request.POST.get('userName')
        password = request.POST.get('passWord')
        user = authenticate(request, username=username,password=password)
        if user is not None:
            login(request, user)
            return redirect('public_dashboard')
        else:
            messages.error(request,'Usernname or password is incorrect')
    
    return render(request,'user/login.html',{})

@unauthenticated_user
def register(request):
    form = SignupForm(label_suffix='')
    if request.method == 'POST':
        form = SignupForm(request.POST,label_suffix='')
        if form.is_valid():
            form.save()
            messages.success(request,'Account created')
            return redirect('login')
    context = {'form': form}
    return render(request,'user/signup.html',context)
    

def Logout(request):
    messages.success(request,'Successful logout')
    logout(request)
    return redirect('login')