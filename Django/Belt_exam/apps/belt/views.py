# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse, redirect, reverse
from .models import *
from django.contrib import messages
from ..login_and_registration.models import User

# Create your views here.
def index(request):
    if not 'username' in request.session:#this is the authorization
        messages.error(request, 'PLEASE LOG IN FIRST TO ACCESS TRIPS')
        return redirect('/')
    trip = Trip.objects.all()
    current_user = User.objects.get(id=request.session['user_id'])
    others_trips = Trip.objects.all().exclude(creator=current_user).exclude(travelers=current_user)
    print trip
    joined_trips = Trip.objects.filter(creator=current_user, travelers=current_user),
    my_trips = Trip.objects.all().filter(creator=current_user)
    context = {
        "trips": trip,
        "current_user": current_user,
        "joined_trips": joined_trips,
        "my_trips": my_trips,
        "others_trips": others_trips
    }

    return render(request, 'belt/index.html', context)

def new(request):
    return render(request, 'belt/new.html')

def create(request):
    errors = Trip.objects.trip_validator(request.POST)
    if len(errors):
        for error in errors:
            messages.error(request, errors[error])
        print errors
        return redirect('/belt/new')
    else:
        destination = request.POST['destination']        
        description = request.POST['description']
        current_user = User.objects.get(id=request.session['user_id'])
        new_trip = Trip.objects.create(destination=destination, description=description, creator=current_user)
        print new_trip   
        return redirect('/belt/')

def show(request, id):
    travelers = Trip.objects.get(id=int(id)).travelers.all()
    trip = Trip.objects.get(id=int(id))
    context = {
        "trip": trip,
        "travelers": travelers
    }
    return render(request, "belt/show.html", context)

def joined(request, id):
        current_user = User.objects.get(id=request.session['user_id'])
        trip_joined = Trip.objects.get(id=id)
        trip_joined.travelers.add(current_user)
        # trip_joined.save()
        return redirect('/belt/')

def dropped(request, id):
        current_user = User.objects.get(id=request.session['user_id'])
        trip_joined = Trip.objects.get(id=id)
        trip_joined.travelers.remove(current_user)
        # trip_joined.save() #not really neccessary
        return redirect('/belt/')

def edit(request, id):
    trip = Trip.objects.get(id=int(id))
    context = {
		"trip": trip
        }
    print trip.creator.id
    print request.session['user_id']
    if  trip.creator.id == request.session['user_id']:
        return render(request, "belt/edit.html", context)    
    else:
        messages.error(request, 'SORRY, ONLY THE CREATOR CAN REMOVE A TRIP.')
        return redirect('/belt/')

def delete(request,id):
    # trip = Trip.objects.get(id=int(id))
    Trip.objects.get(id=int(id)).delete()
    # if  trip.creator.id == request.session['user_id']:
    #     messages.error(request, 'TRIP SUCCESSFULLY REMOVED.')
    #     return redirect('/belt/')    
    # else:
    #     messages.error(request, 'SORRY, ONLY THE CREATOR CAN REMOVE A TRIP.')
    return redirect('/belt/')
       

