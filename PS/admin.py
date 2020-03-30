from django.contrib import admin

# Register your models here.

from .models import ProblemStatement,Answer,Root

admin.site.register(ProblemStatement)
admin.site.register(Answer)
admin.site.register(Root)
