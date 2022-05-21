from django.db import models
from django.conf import settings


class Genre(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Actor(models.Model):
    name = models.CharField(max_length=150)

    def __str__(self):
        return self.name


class Director(models.Model):
    name = models.CharField(max_length=150)

    def __str__(self):
        return self.name    


class Movie(models.Model):
    genres = models.ManyToManyField(Genre)
    actor = models.ManyToManyField(Actor)
    director = models.ManyToManyField(Director)
    title = models.CharField(max_length=120)
    overview = models.TextField()
    # vote_average = models.FloatField()
    release_date = models.DateField()
    poster_url = models.CharField(max_length=200)

    def __str__(self):
        return f'{self.title} ({self.release_date})'


class Review(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name="reviews")
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="reviews")
    content = models.CharField(max_length=200)
    vote_rate = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.movie}의 comment: ({self.content})'