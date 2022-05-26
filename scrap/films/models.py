
from django.db import models

# Create your models here.

class Films(models.Model):
    rang=models.IntegerField(null=True)
    movie_name = models.CharField(max_length=80,null=True)
    year = models.PositiveIntegerField(null=True)
    time = models.PositiveIntegerField(null=True)
    rating = models.PositiveIntegerField(null=True)
    votes = models.BigIntegerField(null=True)
    gross = models.CharField(max_length=80,null=True)
    director = models.CharField(max_length=100,null=True)
    stars = models.TextField(null=True)
    
