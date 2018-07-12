# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, HttpResponse, redirect
from time import gmtime, strftime, localtime


def index(request):
    current_time = {
        "gmdate": strftime("%Y-%m-%d", gmtime()),
        "gmtime": strftime("%H:%M %p", gmtime()),
        "lcdate": strftime("%Y-%m-%d", localtime()),
        "lctime": strftime("%H:%M %p", localtime()),
    }
    return render(request,'temp/current_time.html', current_time)
    #response = "Hello, I am your first request!"
    #return HttpResponse(response)

#def display(request):
    #response = "The time now is...."
    #return HttpResponse(response)
