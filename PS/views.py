from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
# Create your views here.

from accounts.models import UserDetail
from .models import Tag, Category, ProblemStatement, Answer
from .forms import AddResponseForm

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
    replies = []
    if answers.count() != 0:
        node = answers.get(a_number=a_id)
        collect_answers(replies,node,statement)
    context = {
        'user' : user,
        'statement': statement,
        'answers':answers,
        'replies':replies,
    }
    return render(request,'app/answer.html',context)

@login_required(login_url = 'login')
def add_answer(request,id):
    user = UserDetail.objects.get(user=request.user)
    statement = ProblemStatement.objects.get(id=id)
    form = AddResponseForm()
    if request.method == 'POST':
        form = AddResponseForm({
            'csrfmiddlewaretoken': request.POST['csrfmiddlewaretoken'],
            'answer': request.POST['answer'],
            'statement':statement,
            'givenBy': [user],
            'a_parent': None,
            'a_number': statement.count+1
        })
        if form.is_valid():
            form.save()
            statement.count=statement.count+1
            statement.save()
            return redirect('../../response/'+id+'/'+str(statement.count))
    context = {
        'form' : form,
        'user' : user,
        'statement': statement,
    }
    return render(request,'app/create.html',context)

def collect_answers(replies,node,statement):
    replies.append(node)
    answers = statement.PS.filter(a_parent=node)
    for ans in answers :
        collect_answers(replies,ans,statement)
    return replies
