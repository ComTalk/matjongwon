from rest_framework import serializers

from .models import Place

class PlaceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Place
        fields = '__all__'

class PlaceSearchSerializer(serializers.ModelSerializer):
    class Meta:
        model = Place
        fields = ('name', 'category', 'address', 'menu', 'description')
