# pages/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.IndexPageView, name='index'),
    # path('quiz/', views.QuizPageView, name='quiz'),
    path('contact/', views.ContactPageView, name='contact'),
    path('about/', views.AboutPageView, name='about'),
]