from django import forms
from .models import *

class BidCreation(forms.Form):
    image = forms.CharField()
    name = forms.CharField()
    description = forms.CharField()
    amount_initial= forms.IntegerField()
    time_limit = forms.DateTimeField(widget=forms.DateTimeInput(attrs={'type': 'datetime-local'}))
    class Meta:
        model = Bid_posts
        fields = ['image', 'name','description','amount_initial', 'time_limit']


class BidUpdation(forms.Form):
    image = forms.CharField()
    name = forms.CharField()
    description = forms.CharField()
    amount_initial= forms.IntegerField()
    time_limit = forms.DateTimeField()
    class Meta:
        model = Bid_posts
        fields = ['image', 'name','description','amount_initial', 'time_limit']
