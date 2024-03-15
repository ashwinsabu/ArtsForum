from django.urls import path
from . import views

urlpatterns = [
    path('', views.communityPageView, name='index_comm'),
    path('book/<int:id>/', views.bookPageView, name='booking'),
    ]