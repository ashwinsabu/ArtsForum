"""Bids module for displaying arts"""
from django import forms
from django.core import validators
from django.utils import timezone
from .models import *


class BidCreation(forms.Form):
    """Class for form to create a bid"""

    def __init__(self):
        pass
    image = forms.ImageField()
    len_max = 20
    len_min = 2
    message_min = f"Should have at least {len_min} characters."
    message_max = f"Should have at most{len_max} characters."
    name = forms.CharField(validators=[
    validators.MinLengthValidator(len_min, message_min),
    validators.MaxLengthValidator(len_max, message_max)
    ])

    len_max_des=200
    message_max_des = f"Must have at most{len_max_des} characters."
    description = forms.CharField(validators=[
    validators.MinLengthValidator(len_min, message_min),
    validators.MaxLengthValidator(len_max_des, message_max_des)
    ])

    amount_initial= forms.IntegerField()
    def checktime(self,value):
        """Function for checking if the time is past"""
        if value<timezone.now():
            raise forms.ValidationError("Select a future time")
        # elif value

    time_limit = forms.DateTimeField(
        widget=forms.DateTimeInput(
            attrs={'type': 'datetime-local'}),
            validators=[checktime])

    class Meta:
        """Class for forms of Bids"""
        model = BidPosts
        fields = ['image', 'name','description','amount_initial', 'time_limit']


# class BidUpdation(forms.Form):
#     image = forms.CharField()
#     name = forms.CharField()
#     description = forms.CharField()
#     amount_initial= forms.IntegerField()
#     time_limit = forms.DateTimeField()
#     class Meta:
#         model = BidPosts
#         fields = ['image', 'name','description','amount_initial', 'time_limit']
