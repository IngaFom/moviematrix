from django.db import models
from django.contrib.auth.models import User


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(blank=True)
    # Add other fields as needed

    def __str__(self):
        return self.user.username


class Movie(models.Model):
    title = models.CharField(
        max_length=200,
        null=False,
        blank=False,
    )
    release_date = models.DateField(
        null=False,
        blank=False,
    )
    director = models.ForeignKey(
        'Director',
        on_delete=models.PROTECT,
        null=False,
        blank=False,
    )
    actors = models.ManyToManyField(
        'Actor',
        blank=False,
    )
    genres = models.ManyToManyField(
        'Genre',
        blank=False,
    )

    categories = models.ManyToManyField(
        'Category',
        blank=True,
    )

    def __str__(self):
        return self.title


class Director(models.Model):
    name = models.CharField(max_length=200,
                            null=False,
                            blank=False,
                            )
    gender = models.CharField(max_length=15,
                              null=False,
                              blank=False,
                              )
    birthday = models.DateField(null=False,
                                blank=False,
                                )

    def __str__(self):
        return self.name


class Actor(models.Model):
    name = models.CharField(max_length=200,
                            null=False,
                            blank=False,
                            )
    gender = models.CharField(max_length=15,
                              null=False,
                              blank=False,
                              )
    birthday = models.DateField(null=False,
                                blank=False,
                                )

    def __str__(self):
        return self.name


class Genre(models.Model):
    id = models.IntegerField
    name = models.CharField(max_length=150,
                            null=False,
                            blank=False,
                            )

    def __str__(self):
        return self.name

    class Category(models.Model):
        name = models.CharField(max_length=150,
                                null=False,
                                blank=False,
                                )

        def __str__(self):
            return self.name




