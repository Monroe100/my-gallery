# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
import datetime as dt
# Create your models here.

class Location(models.Model):
    location = models.CharField(max_length=60)


    def save_locations(self):
        self.save()

    
    def delete_locations(self):
        self.delete()
    
    def __str__(self):
        return self.location


class Category(models.Model):
    name = models.CharField(max_length=30, blank=True)

    
     def save_category(self):
        self.save()

    def delete_category(self):
        self.delete()