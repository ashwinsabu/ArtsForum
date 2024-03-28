"""Community module for displaying arts"""
from django.shortcuts import render, redirect
from .models import *
from .forms import *
import json
from django.contrib import messages
from django.urls import reverse
# Create your views here.

def communityPageView(request):
    """Function for displaying the events for users"""
    if request.user.is_authenticated:
        if request.method == 'POST':
            if 'book_me' in request.POST:
                community_id = request.POST.get('id')
                community_sec = Community.objects.get(id=community_id)
                if (community_sec.seats > 0):
                    community_sec.seats-=1
                    add=Participants.objects.create(
                        user_id=request.user,
                        community_id=community_sec,
                        name=request.user.username,
                        email=request.user.email
                    )
                    community_sec.save()
                return redirect('index_comm')
            elif 'cancel' in request.POST:
                community_id = request.POST.get('id')
                community_sec = Community.objects.get(id=community_id)
                community_sec.seats+=1
                community_sec.save()
                remove = Participants.objects.filter(community_id=community_id,user_id=request.user)
                remove.delete()
                return redirect('index_comm')
        # To get the data for users already registered for event
        participants=Participants.objects.filter(user_id=request.user).values_list('community_id', flat=True).distinct()
        communities_registered = Community.objects.filter(id__in=participants)

        # To get the data for not registered for event
        communities_notregistered = Community.objects.exclude(id__in=participants).exclude(seats=0)
        context= {
            "community":communities_notregistered,
            "communities_registered":communities_registered,
            "participants":participants
        }
        return render(request, 'index_comm.html',context)
    else:
        return redirect('login')

def bookPageView(request,id):
    """Function for booking the events for users"""
    if request.user.is_authenticated:
        if request.method == 'POST':
            participants = request.POST.get('participants')
            if participants:
                participants = json.loads(participants)
                print(len(participants))
                community=Community.objects.get(id=id)
                if(community.seats>=len(participants)):
                    for x in participants:
                        participant = Participants.objects.create(
                            name=x['name'],
                            email=x['email'],
                            age=x['age'],
                            number=x['number'],
                            user_id=request.user,
                            community_id= community
                        )
                else:
                    messages.warning(request, f'Only {community.seats} seats are remaining in this community.')

                return redirect(reverse('booking', args=[id]))

        return render(request, 'booking.html')
    else:
        return redirect('login')

def CreatePageView(request):
    """Function for creataing the events for volunteers/supervisors"""
    if request.user.is_authenticated and request.user.is_staff==True:
        if request.method == 'POST':
            form = EventCreation(request.POST)
            if form.is_valid():
                seats = form.cleaned_data['seats']
                heading = form.cleaned_data['heading']
                location = form.cleaned_data['location']
                subline = form.cleaned_data['subline']
                event = Community.objects.create(
                    seats=seats,
                    heading=heading,
                    location=location,
                    subline=subline,
                    user_id=request.user
                )
                return redirect('index_comm')
        elif request.method == "GET":
            form = EventCreation()
        return render(request, 'create_event.html', {'form': form})
    else:
        return redirect('login')

def ViewPart(request,id):
    """Function for viewing the participants of the events for volunteers/supervisors"""
    data=Participants.objects.filter(community_id=id)
    context={
        "data":data
    }
    return render(request, 'partdata.html',context)

# def EventDelete(request,id):
#     """Function for deleting the events for volunteers/supervisors"""
#     data=Community.objects.filter(id=id)
#     data.delete()
#     return redirect('mybid.html')

def EventDelete(request, id):
    """Function for deleting the events for volunteers/supervisors"""
    if request.user.is_authenticated:
        data = Community.objects.get(id=id)
        data.delete()
        return redirect('myposts')
    else:
        return redirect('login')
