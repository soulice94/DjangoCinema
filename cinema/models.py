from django.db import models

class Genre(models.Model):
    name = models.CharField(max_length=100)

class Movie(models.Model):
    name = models.CharField(max_length=100)
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE)

class Artist(models.Model):
    name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)

class Performs(models.Model):
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)

