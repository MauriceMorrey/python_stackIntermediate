# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages

from .models import *
# Create your views here.

def index(request):
    users = User.objects.all()
    return render(request, 'semi/index.html',{'users':users})

def new(request):
    return render(request, "semi/new.html")

def create(request):
    errors = User.objects.basic_validator(request.POST)
    if len(errors):
        for error in errors:
            messages.error(request, errors[error])
        print errors
        return redirect("/new")
    else:
        first_name = request.POST["first_name"]
        last_name = request.POST["last_name"]
        email = request.POST["email"]
        new_user = User.objects.create(first_name=first_name, last_name=last_name, email=email)
        print new_user    
        return redirect("/{}/show".format(new_user.id))# shows information of the new user using the new id created
        
def show(request, id):
    context = {
		"user": User.objects.get(id=int(id))
	}
    return render(request, "semi/show.html", context)

    # user_id = User.objects.get(id = id)
    # print user_id
    # return render(request, "semi/show.html",{'user_id': user_id})

def edit(request, id):
    context = {
		"user": User.objects.get(id=int(id))
	}
    return render(request, "semi/edit.html", context)

    # user_id = User.objects.get(id = id)
    # return render(request, "semi/edit.html",{'user_id':user_id})

def update(request, id):
    errors = User.objects.basic_validator(request.POST)
    if len(errors):
        for error in errors:
            messages.error(request, errors[error])
        print errors
        return redirect("/{}/edit".format(id))#curly braces grab the information, in this case the id that we need and output it
    else:
        #user = User.objects.get(id=id)
        first_name = request.POST["first_name"]
        last_name = request.POST["last_name"]
        email = request.POST["email"]
        #user.save()
        User.objects.filter(id=id).update(first_name=first_name, last_name=last_name, email=email)
        print email
        return redirect("/{}/show".format(id))

def delete(request, id):
    User.objects.get(id=int(id)).delete()
    # user.delete()
    return redirect("/")


