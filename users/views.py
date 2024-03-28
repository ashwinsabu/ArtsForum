"""Users module for login and signup"""
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login
from .forms import UserSignUpForm,LoginForm

def sign_up(request):
    """Function to create account for users"""
    if request.method == "POST":
        form = UserSignUpForm(request.POST)
        if form.is_valid():
            user=form.save()
            if user:
                return redirect('login')
    elif request.method == "GET":
        form = UserSignUpForm()
    return render(request, 'users/signup.html', {'form': form})

def signin(request):
    """Function to login to account for users"""
    form = LoginForm(request.POST or None)
    msg = None
    if request.method == 'POST':
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('index')
            msg= 'invalid credentials'
        msg = 'error validating form'
    return render(request, 'users/signin.html', {'form': form, 'msg': msg})
