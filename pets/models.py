# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from datetime import datetime

class PetImage(models.Model):
    image = models.ImageField(upload_to="pets/", null=True, blank=True)
    caption = models.CharField(max_length=250)
    def __str__(self):
        return self.caption

class PhotoAlbum(models.Model):
    cover_image = models.ForeignKey(PetImage)
    caption = models.CharField(max_length=250)
    def __str__(self):
        return self.caption

class VideoGallery(models.Model):
    cover_image = models.ForeignKey(PetImage)
    caption = models.CharField(max_length=250)

    def __str__(self):
        return self.caption

class Pet(models.Model):
    age = models.IntegerField(null=True)
    GENDER_CHOICES = (('M', 'Male'), ('F', 'Female'))
    gender = models.CharField(max_length=1, choices = GENDER_CHOICES)
    owner = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    country = models.CharField(max_length=100, null=True, blank=True)
    name = models.CharField(max_length=100)
    nickname = models.CharField(max_length=100, null=True, blank=True)
    breed = models.CharField(max_length=100, null=True, blank=True)
    source = models.CharField(max_length=100, null=True, blank=True)
    colour = models.CharField(max_length=100)
    eye_colour = models.CharField(max_length=100)
    date_arrived = models.DateTimeField(null=True, blank=True)
    story = models.TextField(max_length=500, null=True, blank=True)
    description = models.TextField(max_length=500, null=True, blank=True)
    habits = models.TextField(max_length=500, null=True, blank=True)
    favourites = models.TextField(max_length=500, null=True, blank=True)
    dislikes = models.TextField(max_length=500, null=True, blank=True)
    daily_schedule = models.TextField(max_length=500, null=True, blank=True)
    profile_photo = models.ImageField(upload_to="pet_profiles/", null=True, blank=True)
    cover_photo = models.ImageField(upload_to="pet_covers/", height_field=500, width_field=500, null=True, blank=True)
    date_neutered = models.DateTimeField(null=True, blank=True)
    date_chipped = models.DateTimeField(null=True, blank=True)
    photo_album = models.ForeignKey(PhotoAlbum, null=True, blank=True)
    photo = models.ForeignKey(PetImage, null=True, blank=True)

    def __str__(self):
        return self.name

    def image_tag(self):
        return u'<img src="%s" />' % self.profile_photo.url


class Recipe(models.Model):
    name = models.CharField(max_length=200)
    ingredients = models.TextField(max_length=1000)
    steps = models.TextField(max_length=1000)
    pet = models.ForeignKey(Pet)
    def __str__(self):
        return self.name


class VetVisit(models.Model):
    visit_date = models.DateTimeField(null=True, blank=True)
    description = models.TextField(max_length=500, null=True, blank=True)
    pet = models.ForeignKey(Pet, on_delete=models.CASCADE)
    def __str__(self):
        return "{} on {}".format(self.description, self.visit_date)

class Post(models.Model):
    post_body = models.CharField(max_length=300)
    author = models.ForeignKey(Pet)
    created_at = models.DateTimeField(default=datetime.now())

class Comment(models.Model):
    post_body = models.CharField(max_length=300)
    author = models.ForeignKey(Pet)
    created_at = models.DateTimeField(default=datetime.now())
    to_post = models.ForeignKey(Post)
    EXPRESSION_CHOICES = ((1, 'OMG'), (2, 'Cute'), (3, 'Love'), (4, 'Sad'), (5, 'Default'))
    expression = models.CharField(max_length=1, choices = EXPRESSION_CHOICES)
