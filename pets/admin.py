# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from .models import Pet, Post

admin.site.register(Pet)


admin.site.register(Post)