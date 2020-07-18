import django_filters
from .models import ProblemStatement, Category


class CategoryFilter(django_filters.FilterSet):

    category = django_filters.ModelChoiceFilter(queryset=Category.objects.all())

    class Meta:
        model : ProblemStatement
        fields : '__all__'