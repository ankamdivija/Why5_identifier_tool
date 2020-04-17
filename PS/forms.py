from django import forms

from .models import Answer, ProblemStatement

class AddResponseForm(forms.ModelForm):
    
    class Meta:
        model = Answer
        fields = '__all__'


class AddPost(forms.ModelForm):

    class Meta:
        model = ProblemStatement
        fields = '__all__'
