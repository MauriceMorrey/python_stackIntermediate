# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse, redirect
from .models import Article
#from django.http import HttpResponse

def index(request):
    # response = "Hello, am I your first request?"
    # return HttpResponse(response)
    return render(request, 'temp/index.html')

def test(request):
    articles = Article.objects.all().order_by('date')
    # response = "This works as the first test!"
    # return HttpResponse(response)
    return render(request, 'temp/test.html', {'articles': articles})

def article_details(request, slug):
    #return HttpResponse(slug)
    articles = Article.objects.get(slug=slug)
    return render(request, 'temp/details.html', {'articles': articles})#this gives us the article when we click on the links instead of just returning the slug