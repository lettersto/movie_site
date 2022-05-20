from django.db import models
from django.conf import settings

# Create your models here.
class Genre(models.Model):
    name = models.CharField(max_length=50)

class Actor(models.Model):
    name = models.CharField(max_length=150)

class Director(models.Model):
    name = models.CharField(max_length=150)    

class Movie(models.Model):
    genres = models.ManyToManyField(Genre)
    actor = models.ManyToManyField(Actor)
    director = models.ManyToManyField(Director)
    title = models.CharField(max_length=120)
    overview = models.TextField()
    # vote_average = models.FloatField()
    release_date = models.DateField()
    poster_url = models.CharField(max_length=200)


class Review(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    content = models.CharField(max_length=200)
    vote_rate = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)