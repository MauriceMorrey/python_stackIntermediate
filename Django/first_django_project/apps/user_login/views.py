# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse, redirect
from . models import User

# Create your views here.
def index(request):
    # response = "Hello, am I your first request?"
    # return HttpResponse(response)
    return render(request, 'tem/index.html')

def test(request):
    users = User.objects.all().order_by('created_at')
    # response = "This works as the first test!"
    # return HttpResponse(response)
    return render(request, 'tem/test.html', {'users': users})


