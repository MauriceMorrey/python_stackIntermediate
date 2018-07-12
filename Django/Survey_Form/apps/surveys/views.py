# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse, redirect

def index(request):
    #response = "Hello there!"
    #return HttpResponse(response)
    return render(request, 'temp/surveys.html')

def process(request):# PROCESS IS NOT A PAGE, IT'S THERE TO DO THE HEAVY LIFTING IN THE BACKGROUND
        if 'count' not in request.session:
            request.session['count'] = 1
        else:
            request.session['count'] += 1

        request.session['name'] = request.POST['name']
        request.session['location'] = request.POST['location']
        request.session['language'] = request.POST['language']
        request.session['comment'] = request.POST['comment']
        return redirect('/surveys/result')

def result(request): #THIS WORKS WITH OR WITHOUT THE CONTEXT
    # context = { 
    #     'count': request.session['count'],
    #     'name': request.session['name'],
    #     'location': request.session['location'],
    #     'language': request.session['language'],
    #     'comment': request.session['comment']
    # }
    return render(request, 'temp/result.html')

def reset(request):
    request.session['count'] = 0
    return redirect('/surveys/result')

# Create your views here.
