# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse, redirect
from time import gmtime, strftime, localtime

def index(request):
    #response = "Hi once more!"
    #return HttpResponse(response)
    return render(request, 'temp/session.html')

def add(request):
    if 'new_word' not in request.session:
        request.session['new_word'] = []

    if 'fonts' not in request.POST:
        fonts = 'small'

    else:
        fonts = request.POST['fonts']

    context = {
        "new_word": request.POST["new_word"],
        "time": strftime("%Y-%m-%d %H:%M %p", gmtime()),
        "color": request.POST["color"],
        "fonts": fonts
     }
    new_list = request.session['new_word']
    new_list.append(context)
    request.session['new_word'] = new_list
    
    # request.session['new_word'] = request.POST['new_word']
    # request.session['color'] = request.POST['color']
    return redirect('/')

def clear(request):
    request.session.clear()
    return redirect('/')
