# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse, redirect
from . models import *

# Create your views here.
def index(request):
    # response = "Hello, am I your first request?"
    # return HttpResponse(response)
    return render(request, 'templ/index.html')

def details(request):
    dojos = Dojo.objects.all().order_by('name')
    # response = "This works as the first test!"
    # return HttpResponse(response)
    return render(request, 'templ/details.html', {'dojos': dojos})



