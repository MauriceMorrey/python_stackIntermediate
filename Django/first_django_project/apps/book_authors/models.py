# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Book(models.Model):
    name = models.CharField(max_length = 255)
    desc = models.TextField(max_length = 1000)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)

    def __str__(self):#this makes sure that django returns whatever we name in our Dojo,in our example,state = NY, instead of returning 'object'
        return self.name

    def __repr__(self):
        return "Book object: \n{}\n{}\n{}\n".format(self.id, self.name, self.desc)


class Author(models.Model):
    first_name = models.CharField(max_length = 255)
    last_name = models.CharField(max_length = 255)
    email = models.CharField(max_length = 255)
    books = models.ManyToManyField(Book, related_name="authors")
    notes = models.TextField(default="Author's Notes")
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)

    def __str__(self):#this makes sure that django returns whatever we name in our Dojo,in our example,state = NY, instead of returning 'object'
        return self.first_name

    def __repr__(self):
        return "Author object: \n{}\n{}\n{}\n{}\n{}\n".format(self.id, self.first_name, self.last_name, self.email, self.books)

    