from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from .models import UserDetail

# class Signup(forms.ModelForm):
#     password = forms.CharField(widget=forms.PasswordInput)
#     confirm_password=forms.CharField(widget=forms.PasswordInput())
#     class Meta:
#         model = UserDetail
#         fields = ['username','email', 'first_name', 'last_name', 'password','confirm_password']
    
#     def clean(self):
#         cleaned_data = super(Signup, self).clean()
#         password = cleaned_data.get("password")
#         confirm_password = cleaned_data.get("confirm_password")

#         if password != confirm_password:
#             self.add_error('password', 'Password does not match.')


class SignupForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','email', 'first_name', 'last_name', 'password1','password2']
