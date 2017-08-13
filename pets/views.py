# -*- coding: utf-8 -*-

from rest_framework import generics
from django.views import generic
from .models import Pet, Post, Comment
from .serializers import PetSerializer

class IndexView(generic.ListView):
    model = Pet
    template_name = 'index.html'
    context_object_name = 'all_pets'

    def get_queryset(self):
        return Pet.objects.all()


class DetailView(generic.DetailView):
    template_name = 'details.html'
    model = Pet


class ApiDetails(generics.RetrieveUpdateDestroyAPIView):
    queryset = Pet.objects.all()
    serializer_class = PetSerializer


class BlogView(generic.ListView):
    template_name = 'blog.html'
    model = Post
    context_object_name = 'the_posts'

    def get_context_data(self, **kwargs):
        context = super(BlogView, self).get_context_data(**kwargs)
        context['pet'] = Pet.objects.get(pk=2)
        return context

    def get_queryset(self):
        return Post.objects.filter(author=2)



