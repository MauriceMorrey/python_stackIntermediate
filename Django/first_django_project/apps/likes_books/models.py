# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class User(models.Model):
    first_name = models.CharField(max_length= 255)
    last_name = models.CharField(max_length= 255)
    email = models.CharField(max_length= 255)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    def __str__(self):#this makes sure that django returns whatever we name in our Dojo,in our example,state = NY, instead of returning 'object'
        return self.first_name

    def __repr__(self):
        return "User object: \n{}\n{}\n{}\n{}\n".format(self.id, self.first_name, self.last_name, self.email)


class Book(models.Model):
    name = models.CharField(max_length= 255)
    desc = models.CharField(max_length= 255)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)
    uploader = models.ForeignKey(User, related_name="uploaded_books")
    liked_users = models.ManyToManyField(User, related_name="liked_books")

    def __str__(self):#this makes sure that django returns whatever we name in our Dojo,in our example,state = NY, instead of returning 'object'
        return self.name

    def __repr__(self):
        return "Book object: \n{}\n{}\n{}\n{}\n{}\n".format(self.id, self.name, self.desc, self.uploader, self.liked_users)

    
    
    
    
