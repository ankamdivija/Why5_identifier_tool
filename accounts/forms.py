from django import forms
from .models import UserDetail

class Signup(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model = UserDetail
        fields = ['username','email', 'first_name', 'last_name', 'password']
