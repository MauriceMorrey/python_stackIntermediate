# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse, redirect, reverse
from .models import *
from django.contrib import messages
from ..login_and_registration.models import User


# Create your views here.
def index(request):
    if not 'username' in request.session:#this is the authorization
        messages.error(request, 'PLEASE LOG IN FIRST TO ACCESS COURSES')
        return redirect('/')
    course = Course.objects.all()
    print course
    current_user = User.objects.get(id=request.session['user_id'])
    context = {
        "courses": course,
        "current_user": current_user
    }

    return render(request, 'courses/index.html', context)

# def new(request):
#     return render(request, 'course/new.html')

def create(request):
    errors = Course.objects.course_validator(request.POST)
    if len(errors):
        for error in errors:
            messages.error(request, errors[error])
        print errors
        return redirect(reverse('courses:index'))
    else:
        name = request.POST['name']
        description = request.POST['description']
        current_user = User.objects.get(id=request.session['user_id'])
        new_course = Course.objects.create(name=name, description=description, creator=current_user)
        print new_course    
        # return redirect("/{}/show".format(new_user.id))# shows information of the new user using the new id created
        return redirect(reverse('courses:index'))

def edit(request, id):
    course = Course.objects.get(id=int(id))
    context = {
		"course": course
        }
    print course.creator.id
    print request.session['user_id']
    if  course.creator.id == request.session['user_id']:
        return render(request, "courses/edit.html", context)    
    else:
        messages.error(request, 'SORRY, ONLY THE CREATOR CAN REMOVE A COURSE.')
        return redirect(reverse('courses:index'))

def delete(request,id):
    Course.objects.get(id=int(id)).delete()
    return redirect(reverse('courses:index'))

def joined(request, id):
        current_user = User.objects.get(id=request.session['user_id'])
        course_joined = Course.objects.get(id=id)
        course_joined.students.add(current_user)
        # course_joined.save()
        return redirect(reverse('courses:index'))

def dropped(request, id):
        current_user = User.objects.get(id=request.session['user_id'])
        course_joined = Course.objects.get(id=id)
        course_joined.students.remove(current_user)
        # course_joined.save()
        return redirect(reverse('courses:index'))

def change(request, id):
    course = Course.objects.get(id=int(id))
    context = {
		"course": Course.objects.get(id=int(id))
	}
    if  course.creator.id == request.session['user_id']:
        return render(request, "courses/change.html", context)    
    else:
        messages.error(request, 'SORRY, ONLY THE CREATOR CAN UPDATE A COURSE.')
        return redirect(reverse('courses:index'))

def update(request, id):
    errors = Course.objects.course_validator(request.POST)
    if len(errors):
        for error in errors:
            messages.error(request, errors[error])
        print errors
        return redirect("/{}/change".format(id))#curly braces grab the information, in this case the id that we need and output it
    else:
        name = request.POST['name']
        description = request.POST['description']
        Course.objects.filter(id=id).update(name=name, description=description)
        print name
        return redirect(reverse('courses:index'))
