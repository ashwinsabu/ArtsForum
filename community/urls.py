"""Community module for displaying arts"""
from django.urls import path
from . import views

urlpatterns = [
    path('', views.community_page_view, name='index_comm'),
    path('book/<int:id>/', views.book_page_view, name='booking'),
    path('create', views.create_page_view, name='create_event'),
    path('view/<int:id>', views.view_part, name='view_part'),
    path('event/delete/<int:id>', views.event_delete, name='event_delete'),
    ]
