from django.contrib import admin
from .models import *
from django.contrib.admin import AdminSite
# Register your models here.

admin.site.register(Question)

admin.site.register(Answer)


