from django import forms
from .models import *
from django.core import validators
from django.utils import timezone

class BidCreation(forms.Form):
    image = forms.ImageField()

    min_length = 2
    max_length = 20

    message_lt_min = f"Should have at least {min_length} characters."
    message_ht_max = f"Should have at most{max_length} characters."
    name = forms.CharField(validators=[
    validators.MinLengthValidator(min_length, message_lt_min),
    validators.MaxLengthValidator(max_length, message_ht_max)
    ])

    max_length_des=200
    message_ht_max_des = f"Should have at most{max_length_des} characters."
    description = forms.CharField(validators=[
    validators.MinLengthValidator(min_length, message_lt_min),
    validators.MaxLengthValidator(max_length_des, message_ht_max_des)
    ])

    amount_initial= forms.IntegerField()
    def checktime(value):
        if value<timezone.now():
            raise forms.ValidationError("Select a future time")
        # elif value

    time_limit = forms.DateTimeField(widget=forms.DateTimeInput(attrs={'type': 'datetime-local'}),validators=[checktime])

    class Meta:
        model = Bid_posts
        fields = ['image', 'name','description','amount_initial', 'time_limit']


# class BidUpdation(forms.Form):
#     image = forms.CharField()
#     name = forms.CharField()
#     description = forms.CharField()
#     amount_initial= forms.IntegerField()
#     time_limit = forms.DateTimeField()
#     class Meta:
#         model = Bid_posts
#         fields = ['image', 'name','description','amount_initial', 'time_limit']
