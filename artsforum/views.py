"""Artsforum module for displaying arts -- views to display the content of web application"""
from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import Http404
from .forms import *
from .models import *
from django.contrib.auth import logout

#Views to display index page
def index_page_view(request):
    """Function for displaying index page"""
    #Checks if any submit operation performed
    if request.method == 'POST':
        #previleage for is_staff true users (supervisors) to delete posts displayed
        if 'delete_admin' in request.POST:
            postid=request.POST.get('post_id')
            data=Posts.objects.get(id=postid)
            data.delete()

        return redirect('index')
    #Get all the Post in the Table
    posts = Posts.objects.all()
    print(request.user)
    context = {
    'posts': posts,
  }
    return render(request, 'users/index.html',context)


# View for contact us page
def contact_page_view(request):
    """Function for displaying contact page and takin the input"""
    #Checks if any submit operation performed
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
        # Displays the success message in contact us page (redirect)
        messages.success(request, 'We will contact you back in no time !!!!!!')
        return redirect('contact')
    return render(request, 'users/contact.html')

# View for creating a post
def post_page_view(request):
    """Function for displaying the post creation page"""
    #Checks if user logged in
    if request.user.is_authenticated:
    #Checks if any submit operation performed
        if request.method == "POST":
            form = PostCreation(request.POST,request.FILES)
            print(form)
            if form.is_valid():
                image = form.cleaned_data['image']
                name = form.cleaned_data['name']
                description = form.cleaned_data['description']
                #Create post
                bid_post = Posts.objects.create(
                    image=image,
                    name=name,
                    description=description,
                    user_created=request.user
                )
                return redirect('index')
            else:
                print("error")
        # Display the form field in HTML page
        elif request.method == "GET":
            form = PostCreation()
        return render(request, 'users/create_post.html', {'form': form})
    # If not logged in navigate to Login Page
    else:
        return redirect('login')

# View for about us page
def about_page_view(request):
    """Function for displaying about us page"""
    return render(request, 'users/about.html')

# View for responding to messages from contact us page
def customer_queries(request):
    """Function for displaying customer queries from contact us page"""
    #checks if user is logged in and is_staff is true (Checks if the user is supervisor)
    if request.user.is_authenticated and request.user.is_staff:
        if "change" in request.POST:
            #Update the comments in the table
            comments = request.POST.get('comments')
            id= request.POST.get('id')
            response= UserRequest.objects.get(id=id)
            response.comments=comments
            #Update the status to 1 which indicate the customer query has been responded
            response.status=1
            #Update the user id of the supervisor updated the commects
            response.vol_assign=request.user
            response.save()

            return redirect('query')
        #Filter the request with status 0, that is queries not yet responded
        queries= UserRequest.objects.filter(status=0)
        context = {
            'queries':queries,
        }
        return render(request, 'users/query.html',context)
    else:
        return redirect('login')

#View for updating the posts
def update_page_view(request, id):
    """Function for updaating the posts"""
    #Checks if user logged in
    if request.user.is_authenticated:
        try:
            post = Posts.objects.get(id=id) # Retrive the posts with id passed through the url
        except Posts.DoesNotExist:
            raise Http404("Post does not exist") # Raise an exception

        # Checks if the update is performed
        if request.method == 'POST':
            form = PostCreation(request.POST,request.FILES)
            if form.is_valid():
                post.name = form.cleaned_data['name']
                post.description = form.cleaned_data['description']
                post.image = form.cleaned_data['image']
                post.save()
                return redirect('myposts')
        else:
            form = PostCreation(initial={
                'name': post.name,
                'description': post.description,
                'image': post.image
            })

        return render(request, 'users/update_post.html', {'form': form})
    else:
        return redirect('login')

def logout_user(request):
    """Function for logging out"""
    logout(request)
    return redirect('login')
