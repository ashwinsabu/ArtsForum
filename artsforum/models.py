"""Artsforum module for displaying arts -- models for creating databases"""
from django.db import models
from django.contrib.auth.models import User

# Create your models here.

#model for Posts
class Posts(models.Model):
    image = models.ImageField(upload_to='uploads/posts')
    name = models.CharField(max_length=30)
    description = models.CharField(max_length=200)
    user_created =models.ForeignKey(User, on_delete=models.CASCADE)
    def __str__(self):
        return self.name

#model for contact us page queries
class UserRequest(models.Model):
    name = models.CharField(max_length=30)
    email = models.EmailField()
    message = models.CharField(max_length=200)
    vol_assign = models.ForeignKey(User, on_delete=models.CASCADE,null=True)
    status = models.IntegerField()
    comments = models.CharField(max_length=200,null=True)

    def __int__(self):
        return str(self.name)
