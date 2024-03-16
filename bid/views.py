from django.shortcuts import render,redirect, get_object_or_404
from .models import *
from artsforum.models import *
from .forms import *
from django.contrib.auth.models import User
from django.http import Http404
from datetime import datetime

# Create your views here.

# Display all the bids to the users that have been created
def BidPageView(request):
    #Checks if user logged in
    if request.user.is_authenticated:
        posts = Bid_posts.objects.filter(time_limit__gt=datetime.now())
        #Checks if any submit operation performed
        if request.method == 'POST':
            if 'bid' in request.POST:
                post_id = request.POST.get('post_id')
                amount_final = request.POST.get('amount_final')
                user_id = request.POST.get('user_id')
                if post_id and amount_final:
                    posts = Bid_posts.objects.get(id=post_id)
                    posts.amount_final=amount_final
                    posts.user_assigned_id=user_id
                    posts.save()
            elif 'delete_admin' in request.POST: #Delete Bid 
                postid=request.POST.get('post_id')
                data=Bid_posts.objects.get(id=postid)
                data.delete()
            return redirect('bid_index') 
        context = {
            'posts': posts,
        }
        return render(request, 'bid_index.html',context)
    else:
        return redirect('login') 



#Create a Bid by a user
def CreatePageView(request):
    #Checks if user logged in
    if request.user.is_authenticated:
        if request.method == "POST":
            form = BidCreation(request.POST) #Calls the form for creation of Bid
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
                bid_post = Bid_posts.objects.create(
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
                return redirect('bid_index') #On successful creation of bid, redirect to the bid index page
        elif request.method == "GET":
            form = BidCreation()
        return render(request, 'create.html', {'form': form})
    else:
        return redirect('login') 

def MyPageView(request):
    if request.user.is_authenticated:
        currentuser = request.user
        posts = Bid_posts.objects.filter(user_created=currentuser)
        myposts = Posts.objects.filter(user_created=currentuser)
        context = {
            'posts': posts,
            'myposts':myposts
        }
        return render(request, 'mybid.html',context)
    else:
        return redirect('login') 

def UpdatePageView(request, post_id):
    if request.user.is_authenticated:
        try:
            post = Bid_posts.objects.get(id=post_id)
        except Bid_posts.DoesNotExist:
            raise Http404("Post does not exist")

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
    else:
        return redirect('login')


# To delete a Bid from the section  -- here we pass the id as the argument
def DeleteBidPost(request, post_id):
    if request.user.is_authenticated:
        data = Bid_posts.objects.get(id=post_id)
        data.delete()
        return redirect('myposts')
    else:
        return redirect('login') 
    
# To delete a Post from the section  -- here we pass the id as the argument
def DeleteMyPost(request, post_id):
    if request.user.is_authenticated:
        data = Posts.objects.get(id=post_id)
        data.delete()
        return redirect('myposts')
    else:
        return redirect('login') 



