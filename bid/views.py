from django.shortcuts import render
from .models import *

# Create your views here.
def BidPageView(request):
    posts = Posts.objects.all()
    context = {
    'posts': posts,
  }
    return render(request, 'users/index.html',context)

def IndexPageView(request):
    posts = Posts.objects.all()
    context = {
    'posts': posts,
  }
    return render(request, 'users/index.html',context)