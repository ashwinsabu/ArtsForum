"""Artsforum module for displaying arts -- forms to manage user input"""
from django import forms
from django.core import validators
from .models import Posts


#Form to create a post
class PostCreation(forms.Form):
    """Function for creating a post"""

    # pylint: disable=too-few-public-methods
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

    class Meta:
        """Class for form"""
        model = Posts
        fields = ['image', 'name','description']
