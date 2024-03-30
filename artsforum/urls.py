"""Artsforum module for displaying arts -- broswer urls"""
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index_page_view, name='index'),
    path('contact/', views.contact_page_view, name='contact'),
    path('about/', views.about_page_view, name='about'),
    path('post/', views.post_page_view, name='post'),
    path('query/', views.customer_queries,name='query'),
    path('update/<int:id>',views.update_page_view, name='update'),
    path('logout', views.logout_user, name='logout'),
]
