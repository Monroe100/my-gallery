# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.test import TestCase
from .models import Location,Category,Image
import datetime as dt
# Create your tests here.


class LocationTestClass(TestCase):
    def setUp(self):
        self.test_location = Location(location="nairobi")

    def test_instance(self):
        self.asserTrue(isinstance(self.test_location, Location))

    def test_saving_location(self):
        self.test_location.save_locations()
        location = Location.objects.all()
        self.assertTrue(len(location) > 0) 


    def test_deleting_locations(self):
        self.test_location = Location(location="nairobi")
        self.test_location.save_locations()
        self.test_location.delete_locations()
        locations = Location.objects.all()
        self.assertTrue(len(locations) < 1)




class CategoryTestClass(TestCase):
    def setUp(self):
        self.test = Category(category="Food")

    def test_instance(self):
        self.asserTrue(isinstance(self.test, Image))

    def test_saving_category(self):
        self.test.save_category()
        images = Category.objects.all()
        self.assertTrue(len(images) > 0)

    def test_deleting_category(self):
        self.test = Category(category="Food")
        self.test.save_category()
        self.test.delete_locations()
        locationss = Category.objects.all()
        self.assertTrue(len(locationss) < 1)



class ImageTestClass(TestCase):
    def setUp(self):
        # Location
        self.test_location = Location(location="nairobi")
        self.test_location.save()
        # Category
        self.test_category = Category(category="Food")
        self.test_category.save()
        # Image
        self.test_image = Image(image="testImage",
                                image_url="testImageurl",
                                image_name="Test",
                                description="This is a test",
                                location=self.test_location)
        self.test_image.save()
        self.test_image.category.add(self.test_category)

    def test_instance(self):
        self.asserTrue(isinstance(self.test_image, Image))

    def test_saving_image(self):
        self.test_image.save_image()
        images = Image.objects.all()
        self.assertTrue(len(images) > 0)

    def test_deleting_image(self):
        self.test_image = Image(location="nairobi")
        self.test_image.save_image()
        self.test_image.delete_locations()
        locations = Image.objects.all()
        self.assertTrue(len(locations) < 1)
