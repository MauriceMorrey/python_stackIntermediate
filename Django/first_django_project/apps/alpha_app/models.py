 # -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length = 100)
    slug = models.SlugField()#this is for the url tab
    body = models.TextField()
    date = models.DateTimeField(auto_now_add = True)
    #add in thumbnail later
    #add in author later

    def __str__(self):#this makes sure that django returns whatever we name in our Article,in our example,title = hello world, instead of returning 'object'
        return self.title

    def snippet(self): # this method reduces long articles to short snippets of the length defined
        return self.body[:50] + '...'