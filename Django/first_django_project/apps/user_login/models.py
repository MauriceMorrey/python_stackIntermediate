# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class User(models.Model):
    first_name = models.CharField(max_length = 45)
    last_name = models.CharField(max_length = 45)
    email_address = models.CharField(max_length = 45)
    age = models.IntegerField(default=1)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)

    def __str__(self):#this makes sure that django returns whatever we name in our Article,in our example,title = hello world, instead of returning 'object'
        return self.first_name

    #def __str__(self):
        #return self.last_name
    
    #def __str__(self):
        #return self.age

    def __repr__(self):
        return "User object: \n{}\n{}\n{}\n{}\n{}\n".format(self.id, self.first_name, self.last_name, self.email_address, self.age)