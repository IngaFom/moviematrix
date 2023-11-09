from django.db import models


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
