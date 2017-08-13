# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from .models import Pet, Post, Recipe, VetVisit, Comment

admin.site.register(Pet)

admin.site.register(VetVisit)

admin.site.register(Post)

admin.site.register(Recipe)

admin.site.register(Comment)