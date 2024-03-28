"""Bids module for displaying arts"""
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class BidPosts(models.Model):
    """Class for bids"""
    image = models.ImageField(upload_to='uploads/bid/')
    name = models.CharField(max_length=30)
    description = models.CharField(max_length=200)
    user_created =models.ForeignKey(User, on_delete=models.CASCADE, related_name='created_bids')
    user_assigned =models.ForeignKey(User, on_delete=models.CASCADE,  related_name='assigned_bids')
    amount_initial = models.IntegerField()
    amount_final = models.IntegerField()
    time_limit = models.DateTimeField()
    Status = models.IntegerField()
    def __str__(self):
        return self.name
    