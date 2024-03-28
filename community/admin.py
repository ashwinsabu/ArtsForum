"""Community module for displaying arts"""
from django.contrib import admin
from .models import Community,Participants

# Register your models here.
admin.site.register(Community)
admin.site.register(Participants)
