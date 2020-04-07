from django.db.models.signals import post_save
from django.dispatch import receiver

from django.contrib.auth.models import User
from .models import UserDetail

@receiver(post_save,sender= User)
def create_profile(sender, instance, created, **kwargs):

    if created :
        UserDetail.objects.create(user= instance)
        print('Profile created!')


# @receiver(post_save,sender= User)
# def create_profile(sender, instance, created, **kwargs):

#     if created == False :
#         instance.profile.save()
#         print('Profile updated!')
