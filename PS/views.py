from django.shortcuts import render
from django.contrib.auth.decorators import login_required
# Create your views here.

from accounts.models import UserDetail
from .models import Tag, Category, ProblemStatement, Answer

@login_required(login_url = 'login')
def public_dashboard(request):
    user = request.user
    tags = Tag.objects.all()
    categories = Category.objects.all()
    statements = ProblemStatement.objects.all()
    context = {
       'user':user,
       'tags':tags,
       'categories':categories,
       'statements':statements,
    }
    return render(request,'app/public_dashboard.html',context)

@login_required(login_url = 'login')
def private_dashboard(request):
    user = request.user
    tags = Tag.objects.all()
    categories = Category.objects.all()
    statements = UserDetail.objects.get(user=user).PS_createdby.all()
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


@login_required(login_url = 'login')
def response(request, id, a_id=1):
    user = request.user
    statement = ProblemStatement.objects.get(id=id)
    answers = statement.PS.filter(a_parent=None)
    # replies = statement.PS.filter(a_parent.answer=)
    context = {
        'user' : user,
        'statement': statement.statement,
        'answers':answers,
    }
    return render(request,'app/answer.html',context)


# def collect_answers()
