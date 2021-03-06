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

    def __str__(self):
        return self.name


class Image(models.Model):
    image = models.ImageField(upload_to='gallery/', blank=True)
    image_url = models.TextField(blank=True)
    image_name = models.CharField(max_length=30, blank=True)
    description = models.TextField(max_length=100, blank=True)
    category = models.ManyToManyField(Category, blank=True)
    post_date = models.DateTimeField(auto_now=True)
    location = models.ForeignKey(Location, blank=True, on_delete=models.CASCADE,)



    def save_image(self):
        self.save()

    def delete_image(self):
        self.delete()


    @classmethod
    def get_all(cls):
        images = cls.objects.order_by('-post_date')
        return images

    @classmethod
    def get_image(cls, id):
        image = cls.objects.get(id=id)
        return image

    @classmethod
    def searched(cls, query):
        
        result = cls.objects.filter(
            description__icontains=query).order_by('-post_date')
        return result