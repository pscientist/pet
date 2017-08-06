from rest_framework import serializers
from .models import Pet

class PetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pet
        fields = ('name', 'breed', 'city', 'country', 'description', 'profile_photo')
