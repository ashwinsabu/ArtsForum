from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Posts(models.Model):
    image = models.CharField(max_length=30)
    name = models.CharField(max_length=30)
    description = models.CharField(max_length=200)
    user_created =models.ForeignKey(User, on_delete=models.CASCADE)
    def __str__(self):
        return self.name
