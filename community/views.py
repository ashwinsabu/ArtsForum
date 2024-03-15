from django.shortcuts import render, redirect
from .models import * 
import json
from django.contrib import messages
from django.urls import reverse
# Create your views here.

def communityPageView(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            if 'book_me' in request.POST:
                community_id = request.POST.get('id')
                community_sec = Community.objects.get(id=community_id)
                if (community_sec.seats > 0):
                    community_sec.seats-=1
                    add=Participants.objects.create(
                        user_id=request.user,
                        community_id=community_sec
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
    if request.user.is_authenticated:
        if request.method == 'POST':
            participants = request.POST.get('participants')
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