from django.db import models
from django.db.models import fields
from rest_framework import serializers
from .models import Films

class NewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Films
        fields = ('rang', 'movie_name', 'year','time','rating','votes','gross','director', 'stars')