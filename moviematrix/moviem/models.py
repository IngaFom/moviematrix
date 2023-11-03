
from django.db import models

# Create your models here.


class Movie(models.Model):
    title = models.CharField(max_length=200)
    release_date = models.DateField()
    director = models.ForeignKey('Director', on_delete=models.SET_NULL, null=True)
    actors = models.ManyToManyField('Actor')
    genres = models.ManyToManyField('Genre')

    def __str__(self):
        return self.title


class Director(models.Model):
    name = models.CharField(max_length=200)
    gender = models.CharField(max_length=15)
    birthday = models.DateField()

    def __str__(self):
        return self.name


class Actor(models.Model):
    name = models.CharField(max_length=200)
    gender = models.CharField(max_length=15)
    birthday = models.DateField()

    def __str__(self):
        return self.name


class Genre(models.Model):
    name = models.CharField(max_length=150)

    def __str__(self):
        return self.name