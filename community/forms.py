from django import forms
from .models import *
from django.core import validators

class EventCreation(forms.Form):
    seats = forms.IntegerField()

    min_length = 2
    max_length = 25

    message_lt_min = f"Should have at least {min_length} characters."
    message_ht_max = f"Should have at most{max_length} characters."
    heading = forms.CharField(validators=[
    validators.MinLengthValidator(min_length, message_lt_min),
    validators.MaxLengthValidator(max_length, message_ht_max)
    ])

    
    location=forms.CharField(validators=[
    validators.MinLengthValidator(min_length, message_lt_min),
    validators.MaxLengthValidator(max_length, message_ht_max)
    ])

    max_length_des=200
    message_ht_max_des = f"Should have at most{max_length_des} characters."
    subline = forms.CharField(validators=[
    validators.MinLengthValidator(min_length, message_lt_min),
    validators.MaxLengthValidator(max_length_des, message_ht_max_des)
    ])

    def clean_seats(self):
        seats = self.cleaned_data.get('seats')
        if seats <=0:
            raise forms.ValidationError("Seat value cannot be less than 0")
        return seats

    class Meta:
        model = Community
        fields = ['seats', 'heading','location', 'subline']

