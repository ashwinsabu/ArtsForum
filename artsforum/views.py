from django.shortcuts import render, redirect
from .models import *
from django.contrib import messages
from .forms import *


# Create your views here.
def IndexPageView(request):
    if request.method == 'POST':
        if 'delete_admin' in request.POST:
            postid=request.POST.get('post_id')
            data=Posts.objects.get(id=postid)
            data.delete()

        return redirect('index')
    posts = Posts.objects.all()
    print(request.user)
    context = {
    'posts': posts,
  }
    return render(request, 'users/index.html',context)

def ContactPageView(request):
    if request.method == "POST":
        name= request.POST.get('name')
        email= request.POST.get('email')
        message= request.POST.get('message')
        create= UserRequest.objects.create(
            name=name,
            email=email,
            message=message,
            status=0
        )
        messages.success(request, 'We will contact you back in no time !!!!!!')
        return redirect('contact')
    return render(request, 'users/contact.html')


def PostPageView(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            form = PostCreation(request.POST)
            if form.is_valid():
                print("Hii")
                image = form.cleaned_data['image']
                name = form.cleaned_data['name']
                description = form.cleaned_data['description']
                bid_post = Posts.objects.create(
                    image=image,
                    name=name,
                    description=description,
                    user_created=request.user
                )
                return redirect('index')
        elif request.method == "GET":
            form = PostCreation()
        return render(request, 'users/create_post.html', {'form': form})
    else:
        return redirect('login') 

def AboutPageView(request):
    return render(request, 'users/about.html')
