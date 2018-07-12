# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

import re
EMAIL_REGEX = re.compile(r"^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$")

# Create your models here.
class UserManager(models.Manager):
    def basic_validator(self, postData):
        errors = {}
        if len(postData['first_name']) < 1:
            errors["first_name"] = "First name should be more than 1 character"
        if len(postData['last_name']) < 1:
            errors["last_name"] = "Last name should be more than 1 character"
        if len(postData["email"]) < 1:
			errors["email"] = "Email address is too short."
        if not EMAIL_REGEX.match(postData['email']):
            errors['email'] = "Invalid email address. Please enter valid email address"
        # if valid == "create":
		# 	if User.objects.filter(email=postData["email"]):
		# 		errors["email"] = "Email address exists. Please use a different email address"
        return errors
class User(models.Model):
    first_name = models.CharField(max_length= 255)
    last_name = models.CharField(max_length= 255)    
    email = models.CharField(max_length= 255)
    created_at = models.TimeField(auto_now_add=True)
    updated_at = models.TimeField(auto_now=True)
    objects = UserManager()

    def __str__(self):
        return self.first_name + self.last_name

    def __repr__(self):
        return "User object: \n{}\n{}\n{}\n{}\n".format(self.id, self.first_name, self.last_name, self.email)

    
    
