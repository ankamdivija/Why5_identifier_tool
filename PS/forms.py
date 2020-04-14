from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from .models import Answer

class AddResponseForm(forms.ModelForm):
    
    class Meta:
        model = Answer
        fields = '__all__'
