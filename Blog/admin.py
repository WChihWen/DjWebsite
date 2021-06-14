from django.contrib import admin
from .models import User, DjangoProject, Courses 
# Register your models here.

admin.site.register(DjangoProject)
admin.site.register(Courses)