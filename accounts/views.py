from django.shortcuts import render , redirect
from django.http import HttpResponse
from .forms import Signup

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
		
def register(request):
    form = Signup()
    if request.method == 'POST':
        #print('printing post req :',request.POST)
        form = Signup(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')

    context = {'form': form}

    return render(request,'user/signup.html',context)

def logout(request):
    return HttpResponse('Logout page')