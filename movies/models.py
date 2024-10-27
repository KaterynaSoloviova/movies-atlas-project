from django.db import models

from datetime import datetime


class Category(models.Model):
    name = models.CharField(verbose_name='Category Name', max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Genre(models.Model):
    name = models.CharField(verbose_name='Genre Name', max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Country(models.Model):
    name = models.CharField(verbose_name='Country Name', max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Actor(models.Model):
    first_name = models.CharField(verbose_name='First Name', max_length=200)
    last_name = models.CharField(verbose_name='Last Name', max_length=200)
    birthday = models.DateTimeField(verbose_name='Birthday')
    country = models.ForeignKey(Country, on_delete=models.SET_NULL, null=True)
    photo = models.ImageField(upload_to='actor_images/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Director(models.Model):
    first_name = models.CharField(verbose_name='First Name', max_length=200)
    last_name = models.CharField(verbose_name='Last Name', max_length=200)
    birthday = models.DateTimeField(verbose_name='Birthday')
    country = models.ForeignKey(Country, on_delete=models.SET_NULL, null=True)
    photo = models.ImageField(upload_to='director_images/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Movie(models.Model):
    title = models.CharField(verbose_name='Title', max_length=200)
    genre = models.ManyToManyField(Genre, related_name='movies')
    year = models.IntegerField(verbose_name='Year')
    country = models.ManyToManyField(Country, related_name='movies')
    photo = models.ImageField(upload_to='movie_images/', blank=True, null=True)
    director = models.ForeignKey(Director, on_delete=models.SET_NULL, null=True)
    actors = models.ManyToManyField(Actor, related_name='movies')
    rating = models.DecimalField(max_digits=3, decimal_places=1, blank=True, null=True)
    imdb_rating = models.DecimalField(max_digits=3, decimal_places=1, blank=True, null=True)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.title} ({self.year})"
