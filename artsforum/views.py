from django.shortcuts import render
from .models import *

# Create your views here.
def IndexPageView(request):
    posts = Posts.objects.all()
    context = {
    'posts': posts,
  }
    return render(request, 'users/index.html',context)

def ContactPageView(request):
    return render(request, 'users/contact.html')

def AboutPageView(request):
    return render(request, 'users/about.html')
