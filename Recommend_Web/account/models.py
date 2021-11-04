from django.db import models
from rest_framework import serializers

# Create your models here.
class Accounts(models.Model):
    username = models.CharField(max_length=30)
    password = models.CharField(max_length=200, default='')
    key = models.CharField(max_length=100, default='')
    favorite = models.CharField(max_length=100, default='', blank=True)
    favorite_rank = models.TextField(default='{}', blank=True)
    role = models.CharField(max_length=30, default='member')
    token = models.CharField(max_length=100, default='', blank=True)



class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Accounts
        fields = '__all__'
