"""Community module for displaying arts"""
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Community(models.Model):
    heading=models.CharField(max_length=30)
    location=models.CharField(max_length=30)
    subline=models.CharField(max_length=200)
    seats = models.IntegerField()
    user_id =models.ForeignKey(User, on_delete=models.CASCADE,null=True)
    def __str__(self):
        return self.heading


class Participants(models.Model):
    name = models.CharField(max_length=30,null=True)
    email = models.EmailField(null=True)
    age = models.IntegerField(null=True)
    number = models.IntegerField(null=True)
    user_id =models.ForeignKey(User, on_delete=models.CASCADE)
    community_id =models.ForeignKey(Community, on_delete=models.CASCADE)
    def __str__(self):
        return str(self.user_id)