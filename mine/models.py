# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
import datetime as dt
# Create your models here.

class Location(models.Model):
    location = models.CharField(max_length=60)


    def save_locations(self):
        self.save()