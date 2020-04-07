from django.shortcuts import render
from django.contrib.auth.decorators import login_required
# Create your views here.

@login_required(login_url = 'login')
def dashboard(request):
    user = request.user
    context = {
        'user':user,
    }
    return render(request,'app/dashboard.html',context)