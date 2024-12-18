"""Community module for displaying arts"""
import json
from django.shortcuts import render, redirect
from django.contrib import messages
from django.urls import reverse
from .models import Community,Participants
from .forms import EventCreation
# Create your views here.

def community_page_view(request):
    """Function for displaying the events for users"""
    if request.user.is_authenticated:
        if request.method == 'POST':
            if 'book_me' in request.POST:
                community_id = request.POST.get('id')
                community_sec = Community.objects.get(id=community_id)
                if community_sec.seats > 0:
                    community_sec.seats-=1
                    add=Participants.objects.create(
                        user_id=request.user,
                        community_id=community_sec,
                        name=request.user.username,
                        email=request.user.email
                    )
                    if add:
                        community_sec.save()
                return redirect('index_comm')
            #Following statements executes when cancel ooperation is passed
            community_id = request.POST.get('id')
            community_sec = Community.objects.get(id=community_id)
            community_sec.seats+=1
            community_sec.save()
            remove = Participants.objects.filter(community_id=community_id,user_id=request.user)
            remove.delete()
            return redirect('index_comm')
        # To get the data for users already registered for event
        participants=Participants.objects.filter(
            user_id=request.user).values_list(
                'community_id', flat=True).distinct()
        communities_registered = Community.objects.filter(id__in=participants)

        # To get the data for not registered for event
        communities_notregistered = Community.objects.exclude(id__in=participants).exclude(seats=0)
        context= {
            "community":communities_notregistered,
            "communities_registered":communities_registered,
            "participants":participants
        }
        return render(request, 'index_comm.html',context)
    return redirect('login')

def book_page_view(request,id_u):
    """Function for booking the events for users"""
    if request.method == 'POST':
        participants = request.POST.get('participants')
        if participants:
            participants = json.loads(participants)
            community=Community.objects.get(id=id_u)
            if community.seats>=len(participants) :
                for x in participants:
                    Participants.objects.create(
                        name=x['name'],
                        email=x['email'],
                        age=x['age'],
                        number=x['number'],
                        user_id=request.user,
                        community_id= community
                    )

            else:
                messages.warning(
                    request, f'Only {community.seats} seats are remaining.')

            return redirect(reverse('booking', args=[id_u]))

    return render(request, 'booking.html')

def create_page_view(request):
    """Function for creataing the events for volunteers/supervisors"""
    if request.user.is_authenticated and request.user.is_staff:
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
                if event:
                    return redirect('index_comm')
        elif request.method == "GET":
            form = EventCreation()
        return render(request, 'create_event.html', {'form': form})
    return redirect('login')

def view_part(request,id_u):
    """Function for viewing the participants of the events for volunteers/supervisors"""
    data=Participants.objects.filter(community_id=id_u)
    context={
        "data":data
    }
    return render(request, 'partdata.html',context)

def event_delete(request, id_u):
    """Function for deleting the events for volunteers/supervisors"""
    if request.user.is_authenticated:
        data = Community.objects.get(id=id_u)
        data.delete()
        return redirect('myposts')
    return redirect('login')
