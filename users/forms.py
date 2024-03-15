from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.core import validators

class UserSignUpForm(UserCreationForm):
    email = forms.EmailField()

    min_length = 2
    max_length = 30
    message_lt_min = f"Should have at least {min_length} characters."
    message_ht_max = f"Should have at most{max_length} characters."
    first_name = forms.CharField(validators=[
    validators.MinLengthValidator(min_length, message_lt_min),
    validators.MaxLengthValidator(max_length, message_ht_max)
    ])
    last_name = forms.CharField(validators=[
    validators.MinLengthValidator(min_length),
    validators.MaxLengthValidator(max_length)
    ])
    username = forms.CharField(validators=[
    validators.MinLengthValidator(min_length),
    validators.MaxLengthValidator(max_length)
    ])

    def clean_password1(self):

        return super().clean_password2()


    class Meta:
        model = User
        fields = ['username', 'first_name','last_name','email', 'password1', 'password2']

class LoginForm(forms.Form):
    username = forms.CharField(
        widget= forms.TextInput(
            attrs={
                "class": "form-control"
            }
        )
    )
    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control"
            }
        )
    )
 