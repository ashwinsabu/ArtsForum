"""Bids module for displaying arts"""
from django.urls import path
from . import views

urlpatterns = [
    path('', views.bid_page_view, name='bid_index'),
    path('create/', views.create_page_view, name='create_bid'),
    path('<int:post_id>', views.update_page_view, name='update_bid'),
    path('myposts/', views.my_page_view, name='myposts'),
    path('delete/<int:post_id>', views.delete_bid_post, name='deletepost'),
    path('post/delete/<int:post_id>', views.delete_my_post, name='delete_my_post'),
]
