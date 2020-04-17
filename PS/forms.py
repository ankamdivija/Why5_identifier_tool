from django import forms

from .models import Answer, ProblemStatement

class AddResponseForm(forms.ModelForm):
    
    class Meta:
        model = Answer
        fields = '__all__'


class AddPost(forms.ModelForm):

    #category = forms.ModelChoiceField(widget=forms.Select(attrs={"class": "category"}), queryset=Category.objects.all())
    class Meta:
        model = ProblemStatement
        fields = '__all__'
