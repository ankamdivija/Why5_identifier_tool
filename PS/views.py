from django.shortcuts import render
from django.contrib.auth.decorators import login_required
# Create your views here.

from accounts.models import UserDetail
from .models import Tag, Category, ProblemStatement

@login_required(login_url = 'login')
def public_dashboard(request):
    user = request.user
    tags = Tag.objects.all()
    #statements = UserDetail.objects.get(user=user).PS_createdby.all()
    #print(statements)
    #context = {
     #   'user':user,
      #  'tags':tags,
       # 'statements':statements,
   # }'''
    return render(request,'app/public_dashboard.html',{})


'''@login_required(login_url = 'login')
def create_post(request):
    user = request.user
    context = {
        'user':user,
    }
    return render(request,'app/create.html',context)'''


@login_required(login_url = 'login')
def private_dashboard(request):
    user = request.user
    tags = Tag.objects.all()
    categories = Category.objects.all()
    statements = UserDetail.objects.get(user=user).PS_createdby.all()
    print(statements)
    context = {
        'user':user,
        'tags':tags,
        'categories':categories,
        'statements':statements,
    }
    return render(request,'app/private_dashboard.html',context)

@login_required(login_url = 'login')
def create_topic(request):
    user = request.user
    context = {
        'user' : user,
    }
    return render(request,'app/create-topic.html',context)
