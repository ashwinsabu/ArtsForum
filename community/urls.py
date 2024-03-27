from django.urls import path
from . import views

urlpatterns = [
    path('', views.communityPageView, name='index_comm'),
    path('book/<int:id>/', views.bookPageView, name='booking'),
    path('create', views.CreatePageView, name='create_event'),
    path('view/<int:id>', views.ViewPart, name='viewpart'),
    path('event/delete/<int:id>', views.EventDelete, name='viewpart'),
    ]