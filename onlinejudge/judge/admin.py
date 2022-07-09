from django.contrib import admin

from .models import Problem, Testcases, Submissions

admin.site.register(Problem)
admin.site.register(Testcases)
admin.site.register(Submissions)
# Register your models here.
