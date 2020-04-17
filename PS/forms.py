from django import forms

from .models import Answer, ProblemStatement

class AddResponseForm(forms.ModelForm):
    
    class Meta:
        model = Answer
        fields = '__all__'


class AddPostForm(forms.ModelForm):
    visibility = forms.ChoiceField(widget=forms.RadioSelect,choices=ProblemStatement.VISIBLITY_CHOICES)
    #category = forms.ModelChoiceField(widget=forms.Select(attrs={"class": "category"}), queryset=Category.objects.all())
    class Meta:
        model = ProblemStatement
        fields = '__all__'
