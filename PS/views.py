from django.shortcuts import render
from django.contrib.auth.decorators import login_required
# Create your views here.

from accounts.models import UserDetail
from .models import Tag, ProblemStatement

@login_required(login_url = 'login')
def dashboard(request):
    user = request.user
    tags = Tag.objects.all()
    statements = UserDetail.objects.get(user=user).PS_createdby.all()
    print(statements)
    context = {
        'user':user,
        'tags':tags,
        'statements':statements,
    }
    return render(request,'app/dashboard.html',context)