"""Artsforum module for displaying arts"""
from django.contrib import admin
from .models import Posts,UserRequest

# Register your models here.
admin.site.register(Posts)
admin.site.register(UserRequest)
