# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse, redirect
from django.utils.crypto import get_random_string

def index(request):
    context = {
        'count': request.session['count'],
        'random_word': get_random_string(length=14) ,
    }
    if 'random_word' not in request.session:
        request.session['random_word'] = ""
    if 'count' not in request.session:
        request.session['count'] = 0
    return render(request,'temp/random_word.html', context)

def generate(request):
    request.session['count'] += 1
    return redirect('/random_word/index')

def reset(request):
    request.session['count'] = 0
    return redirect('/random_word/index')
    #response = "Random word generator"
    #return HttpResponse(response)

# Create your views here.
