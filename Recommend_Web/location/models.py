from django.db import models
from rest_framework import serializers

# Create your models here.
class Locations(models.Model):
    title = models.CharField(max_length=30)
    description = models.CharField(max_length=500)
    count_click = models.IntegerField()
    category = models.CharField(max_length=200)

class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Locations
        field = ['title', 'description', 'count_click', 'category']