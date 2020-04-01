from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    # return HttpResponse('Home page')
    return render(request,'home.html',{})

def login(request):
    return HttpResponse('Login page')

def signup(request):
    return HttpResponse('Signup page')

def logout(request):
    return HttpResponse('Logout page')