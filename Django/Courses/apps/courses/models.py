# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from ..login_and_registration.models import User

# Create your models here.
class CourseManager(models.Manager):
    def course_validator(self, postData):
        errors = {}
        if len(postData['name']) < 5:
            errors['name'] = 'Course name should be more than 5 characters'
        if len(postData['description']) < 15:
            errors['description'] = 'Description should be more than 15 characters'
        return errors

class Course(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(max_length=1000)
    date_added = models.DateField(auto_now_add=True)
    creator = models.ForeignKey(User, related_name='Courses_created')
    students = models.ManyToManyField(User, related_name='Courses_joined')
    objects = CourseManager()

    def __str__(self):
        return self.name

    def __repr__(self):
        return "User object: \n{}\n{}\n{}\n{}\n{}\n".format(self.id, self.name, self.description, self.date_added, self.creator)
