from django.db import models
from accounts.models import UserDetail

# Create your models here.

class Tag(models.Model):
    COLORS = (
        ('bg-4f80b0','blue'),
        ('bg-424ee8','purple'),
        ('bg-36b7d7','sky blue'),
        ('bg-ef429e','dark grey'),
        ('bg-7cc576','green'),
        ('bg-6f7e9c','grey'),
        ('bg-f26522','orange'),
        ('bg-a3d39c','light green'),
        ('bg-92278f','pink'),
    )
    name = models.CharField(max_length=25,null= True)
    color = models.CharField(max_length=25,null= True,choices=COLORS)
    # number = models.CharField(max_length=25,null= True,choices=COLORS)

    def __str__(self):
        return self.name

class Category(models.Model):
    COLORS = (
        ('bg-4f80b0','blue'),
        ('bg-424ee8','purple'),
        ('bg-36b7d7','sky blue'),
        ('bg-ef429e','dark grey'),
        ('bg-7cc576','green'),
        ('bg-6f7e9c','grey'),
        ('bg-f26522','orange'),
        ('bg-a3d39c','light green'),
        ('bg-92278f','pink'),
    )
    name = models.CharField(max_length=25,null= True)
    color = models.CharField(max_length=25,null= True,choices=COLORS)

    def __str__(self):
        return self.name

class ProblemStatement(models.Model):
    VISIBLITY_CHOICES = (
        ('E', 'Everyone'),
        ('M', 'Only Me'),
    )
    STATUS_OPTIONS = (
        ('C','Just Created'),
        ('A','Under Analysis'),
        ('F','Found Root'),
        ('T','Terminated'),
    )
    statement = models.CharField(max_length=100,null=True)
    category = models.ManyToManyField(Category,related_name='category')
    description = models.CharField(max_length=200,null=True)
    createdBy = models.ForeignKey(UserDetail,on_delete=models.CASCADE,related_name='PS_createdby')
    assignees = models.ManyToManyField(UserDetail,related_name='PS_assignee')
    tags = models.ManyToManyField(Tag,related_name='tag')
    status = models.CharField(max_length=20,choices = STATUS_OPTIONS)
    count = models.IntegerField(default=0)
    visibility = models.CharField(max_length=20,choices = VISIBLITY_CHOICES)

    def __str__(self):
        return self.statement


class Answer(models.Model):
    answer = models.CharField(max_length=100,null=True)
    a_parent = models.ForeignKey('self',on_delete=models.CASCADE, null=True, related_name='answer_parent')
    statement = models.ForeignKey(ProblemStatement,on_delete=models.CASCADE,related_name='PS')
    givenBy = models.ManyToManyField(UserDetail,related_name='PS_givenby')
    a_number = models.IntegerField(default=0)

    def __str__(self):
        return "%s - %s" % (self.answer, self.a_number)

    
class Root(models.Model):
    root = models.CharField(max_length=100,null=True)
    statement = models.ForeignKey(ProblemStatement,on_delete=models.CASCADE,related_name='rootOfPS')

    def __str__(self):
        return self.root

