# -*- coding: utf-8 -*-
# Generated by Django 1.11.12 on 2018-04-15 05:14
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book_authors', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='author',
            name='books',
            field=models.ManyToManyField(related_name='authors', to='book_authors.Book'),
        ),
    ]