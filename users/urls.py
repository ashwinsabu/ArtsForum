"""Users module for login and signup"""
from django.urls import path
from . import views

urlpatterns = [
    path('', views.sign_up, name='sign_up'),
    path('login/', views.signin, name='login'),
    ]
