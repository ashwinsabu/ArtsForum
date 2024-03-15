# pages/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.BidPageView, name='bid_index'),
    path('create/', views.CreatePageView, name='create_bid'),
    path('<int:post_id>', views.UpdatePageView, name='update_bid'),
    path('myposts/', views.MyPageView, name='myposts'),
    path('delete/<int:post_id>', views.DeleteBidPost, name='deletepost'),
]