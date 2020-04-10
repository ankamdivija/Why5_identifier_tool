from django.contrib import admin

# Register your models here.

from .models import ProblemStatement,Answer,Root,Tag,Category

admin.site.register(ProblemStatement)
admin.site.register(Answer)
admin.site.register(Root)
admin.site.register(Tag)
admin.site.register(Category)
