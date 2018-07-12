# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from ..login_and_registration.models import User
from datetime import datetime

# Create your models here.
class TripManager(models.Manager):
    def trip_validator(self, postData):
        errors = {}
        if len(postData['destination']) < 5:
            errors['destination'] = 'Destination name should be more than 5 characters'
        if len(postData['description']) < 15:
            errors['description'] = 'Description should be more than 15 characters'
        if len(postData["travel_start_date"])==0:
            errors["travel_start_date"] = "Date cannot be empty!"
        if len(postData["travel_end_date"])==0:
            errors["travel_end_date"] = "Date cannot be empty!"
        print postData["travel_start_date"]
        if postData['travel_start_date'] > postData['travel_end_date']:
            errors['travel_start_date'] = "Start time must be before end time"
        now = datetime.now().strftime("%Y-%m-%d")
        if now > postData['travel_start_date']:
            errors['travel_start_date'] = "Must select a future date"
        return errors

class Trip(models.Model):
    destination = models.CharField(max_length=255)
    description = models.TextField(max_length=1000)
    travel_start_date = models.DateField(auto_now_add=True)
    travel_end_date = models.DateField(auto_now_add=True)    
    creator = models.ForeignKey(User, related_name='Trips_created')
    travelers = models.ManyToManyField(User, related_name='Trips_joined')
    objects = TripManager()

    def __str__(self):
        return self.destination

    def __repr__(self):
        return "User object: \n{}\n{}\n{}\n{}\n{}\n{}\n".format(self.id, self.destination, self.description, self.travel_start_date, self.travel_end_date, self.creator)
