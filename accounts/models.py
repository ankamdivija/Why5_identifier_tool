from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class UserDetail(models.Model):
    # username = models.CharField(max_length=20,null=True)
    user = models.OneToOneField(User,null=True, on_delete = models.CASCADE, related_name='member')
    # first_name = models.CharField(max_length=20,null=True)
    # last_name = models.CharField(max_length=20,null=True)
    # email = models.CharField(max_length=20,null=True)
    # password = models.CharField(max_length=20,null=True)
    full_name = models.CharField(max_length=200,blank=True, null=True)
    proffesion = models.CharField(max_length=200,blank=True, null=True)
    profile_pic = models.ImageField(upload_to="users/" null=True,blank = True,default='users/user.png')
    
    def __str__(self):
        return self.user.username