from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class UserDetail(models.Model):
    username = models.CharField(max_length=20,null=True)
    first_name = models.CharField(max_length=20,null=True)
    last_name = models.CharField(max_length=20,null=True)
    email = models.CharField(max_length=20,null=True)
    password = models.CharField(max_length=20,null=True)

    def __str__(self):
        return self.username