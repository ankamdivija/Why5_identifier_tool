from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
# Create your views here.
from accounts.models import UserDetail
from .models import Tag, Category, ProblemStatement, Answer
from .forms import AddResponseForm, AddPostForm


@login_required(login_url = 'login')
def public_dashboard(request):
    user = request.user
    tags = Tag.objects.all()
    categories = Category.objects.all()
    statements = ProblemStatement.objects.filter(visibility='E')
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
    self_statements = statements.filter(visibility='O')
    statements = statements.filter(visibility='E')
    context = {
        'user':user,
        'tags':tags,
        'categories':categories,
        'statements':statements,
        'self_statements': self_statements,
    }
    return render(request,'app/private_dashboard.html',context)

@login_required(login_url = 'login')
def create_post(request):
    user = UserDetail.objects.get(user=request.user)
    form = AddPostForm()
    if request.method=='POST':
        print(request.POST)
        print(request.POST.getlist('assignees'))
        form = AddPostForm({
            'csrfmiddlewaretoken': request.POST['csrfmiddlewaretoken'],
            'statement': request.POST['statement'],
            'category': request.POST['category'],
            'description': request.POST['description'],
            'createdBy': user,
            'assignees': request.POST.getlist('assignees'),
            'tags': request.POST.getlist('tags'),
            'status':'C',
            'count':0,
            'visibility':request.POST['visibility']
        })
        if form.is_valid():
            form.save()
            return redirect('public_dashboard')
    context = {
        'user' : user,
        'form' : form,
    }
    return render(request,'app/create_post.html',context)


@login_required(login_url = 'login')
def response(request, id, a_id=1):
    user = request.user
    statement = ProblemStatement.objects.get(id=id)
    answers = statement.PS.filter(a_parent=None)
    replies = []
    if answers.count() != 0:
        node = answers.get(a_number=a_id)
        collect_answers(replies,node,statement)
    print(replies)
    context = {
        'user' : user,
        'a_number' : a_id,
        'statement': statement,
        'answers':answers,
        'replies':replies,
    }
    return render(request,'app/sub_response.html',context)

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
            'givenBy': user,
            'a_parent': None,
            'a_number': statement.count+1
        })
        if form.is_valid():
            form.save()
            if(statement.count+1>3):
                statement.status = 'A'
            statement.count=statement.count+1
            statement.save()
            return redirect('../../response/'+id+'/'+str(statement.count))
    context = {
        'form' : form,
        'user' : user,
        'statement': statement,
        'answer' : None,
    }
    return render(request,'app/add_response.html',context)


@login_required(login_url = 'login')
def add_sub_answer(request,id,a_id):
    user = UserDetail.objects.get(user=request.user)
    statement = ProblemStatement.objects.get(id=id)
    answer = Answer.objects.filter(a_number=a_id)
    answer = answer[answer.count()-1]
    form = AddResponseForm()
    if request.method == 'POST':
        form = AddResponseForm({
            'csrfmiddlewaretoken': request.POST['csrfmiddlewaretoken'],
            'answer': request.POST['answer'],
            'statement':statement,
            'givenBy': user,
            'a_parent': answer,
            'a_number': answer.a_number
        })
        if form.is_valid():
            form.save()
            return redirect('../../../response/'+id+'/'+a_id)
    context = {
        'form' : form,
        'user' : user,
        'statement': statement,
        'answer' : answer,
    }
    return render(request,'app/add_response.html',context)


def collect_answers(replies,node,statement):
    replies.append(node)
    answers = statement.PS.filter(a_parent=node)
    for ans in answers :
        collect_answers(replies,ans,statement)
    return replies
