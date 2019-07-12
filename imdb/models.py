# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class imdb(models.Model):
    id = models.IntegerField(primary_key=True)
    moviename = models.CharField(max_length=100,default=' ')
    raing = models.CharField(max_length=10,default=' ')
    star_cast = models.CharField(max_length=300,default=' ')

    class Meta:
        db_table = 'imdb'

    def __str__(self):
        return self.moviename