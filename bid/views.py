"""Bids module for displaying arts"""
from datetime import datetime
from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from artsforum.models import Posts
from community.models import Community
from .models import BidPosts
from .forms import BidCreation

# Create your views here.

# Display all the bids to the users that have been created
def bid_page_view(request):
    """Function for displaying the bids for users"""
    #Checks if user logged in
    if request.user.is_authenticated:
        posts = BidPosts.objects.filter(time_limit__gt=datetime.now())
        #Checks if any submit operation performed
        if request.method == 'POST':
            if 'bid' in request.POST:
                post_id = request.POST.get('post_id')
                amount_final = request.POST.get('amount_final')
                user_id = request.POST.get('user_id')
                if post_id and amount_final:
                    posts = BidPosts.objects.get(id=post_id)
                    posts.amount_final=amount_final
                    posts.user_assigned_id=user_id
                    posts.save()
            elif 'delete_admin' in request.POST: #Delete Bid
                postid=request.POST.get('post_id')
                data=BidPosts.objects.get(id=postid)
                data.delete()
            return redirect('bid_index')
        context = {
            'posts': posts,
        }
        return render(request, 'bid_index.html',context)
    return redirect('login')


#Create a Bid by a user
def create_page_view(request):
    """Function for creating Bid"""
    #Checks if user logged in
    if request.user.is_authenticated:
        if request.method == "POST":
            form = BidCreation(request.POST,request.FILES) #Calls the form for creation of Bid
            if form.is_valid():
                image = form.cleaned_data['image']
                name = form.cleaned_data['name']
                description = form.cleaned_data['description']
                amount_initial = form.cleaned_data['amount_initial']
                time_limit = form.cleaned_data['time_limit']
                user_id = request.POST.get('user_id')
                status = request.POST.get('status')
                amount_final = request.POST.get('amount_final')
                user_assigned = User.objects.get(id=user_id)
                user_created = User.objects.get(id=user_id)
                bid_post = BidPosts.objects.create(
                    image=image,
                    name=name,
                    description=description,
                    amount_initial=amount_initial,
                    time_limit=time_limit,
                    Status=status,
                    amount_final=amount_final,
                    user_assigned=user_assigned,
                    user_created=user_created
                )
                #On successful creation of bid, redirect to the bid index page
                if bid_post:
                    return redirect('bid_index')
        elif request.method == "GET":
            form = BidCreation()
        return render(request, 'create.html', {'form': form})
    return redirect('login')

def my_page_view(request):
    """Function for displaying the contents created by a respective user"""
    if request.user.is_authenticated:
        currentuser = request.user
        posts = BidPosts.objects.filter(user_created=currentuser)
        myposts = Posts.objects.filter(user_created=currentuser)
        community={}
        if request.user.is_staff:
            community=Community.objects.filter(user_id=currentuser)
        context = {
            'posts': posts,
            'myposts':myposts,
            'community':community
        }
        return render(request, 'mybid.html',context)
    return redirect('login')

def update_page_view(request, post_id):
    """Function for Updating the bids"""
    if request.user.is_authenticated:
        post = BidPosts.objects.get(id=post_id)

        if request.method == 'POST':
            form = BidCreation(request.POST)
            if form.is_valid():
                post.name = form.cleaned_data['name']
                post.description = form.cleaned_data['description']
                post.amount_initial = form.cleaned_data['amount_initial']
                post.time_limit = form.cleaned_data['time_limit']
                post.image = form.cleaned_data['image']
                post.save()
                return redirect('myposts')
        else:
            form = BidCreation(initial={
                'name': post.name,
                'description': post.description,
                'amount_initial': post.amount_initial,
                'time_limit': post.time_limit,
                'image': post.image
            })

        return render(request, 'update.html', {'form': form})
    return redirect('login')


# To delete a Bid from the section  -- here we pass the id as the argument
def delete_bid_post(request, post_id):
    """Function for deleting the bids for users"""
    if request.user.is_authenticated:
        data = BidPosts.objects.get(id=post_id)
        data.delete()
        return redirect('myposts')
    return redirect('login')

# To delete a Post from the section  -- here we pass the id as the argument
def delete_my_post(request, post_id):
    """Function for deleting the post for users"""
    if request.user.is_authenticated:
        data = Posts.objects.get(id=post_id)
        data.delete()
        return redirect('myposts')
    return redirect('login')
