# pages/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.IndexPageView, name='index'),
    path('contact/', views.ContactPageView, name='contact'),
    path('about/', views.AboutPageView, name='about'),
    path('post/', views.PostPageView, name='post'),
]