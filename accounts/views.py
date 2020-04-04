from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    # return HttpResponse('Home page')
    return render(request,'user/homepage.html',{})

def login(request):
    return render(request,'user/login.html',{})

def landingpage(request):
	if request.method == 'POST':
		name = request.POST['userName']
		password = request.POST['passWord']
		

def signup(request):
    # return HttpResponse('Signup page')
    return render(request,'user/signup.html',{})

def logout(request):
    return HttpResponse('Logout page')