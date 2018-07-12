# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Dojo(models.Model):
    name = models.CharField(max_length = 255)
    city = models.CharField(max_length = 255)
    state = models.CharField(max_length = 255)
    desc = models.TextField(default="Describe your current dojo experience")

    def __str__(self):#this makes sure that django returns whatever we name in our Dojo,in our example,state = NY, instead of returning 'object'
        return self.name

    def __repr__(self):
        return "Dojo object: \n{}\n{}\n{}\n{}\n".format(self.id, self.name, self.city, self.state)

class Ninja(models.Model):
    first_name = models.CharField(max_length = 255)
    last_name = models.CharField(max_length = 255)
    dojo = models.ForeignKey(Dojo, related_name="ninjas")

    def __str__(self):#this makes sure that django returns whatever we name in our Ninja,in our example,First_name = Leornado, instead of returning 'object'
        return self.first_name    

    def __repr__(self):
        return "Ninja object: \n{}\n{}\n{}\n{}\n".format(self.id, self.first_name, self.last_name, self.dojo)
        

        