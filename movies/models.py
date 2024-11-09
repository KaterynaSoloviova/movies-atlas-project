from django.contrib.auth.models import User
from django.db import models


class Category(models.Model):
    name = models.CharField(verbose_name="Category Name", max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Genre(models.Model):
    name = models.CharField(verbose_name="Genre Name", max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Country(models.Model):
    name = models.CharField(verbose_name="Country Name", max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Actor(models.Model):
    first_name = models.CharField(verbose_name="First Name", max_length=200)
    last_name = models.CharField(verbose_name="Last Name", max_length=200)
    birthday = models.DateField(verbose_name="Birthday", null=True)
    country = models.ForeignKey(Country, on_delete=models.SET_NULL, null=True)
    photo = models.ImageField(upload_to="images/actors", blank=True, null=True)
    biography = models.TextField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Director(models.Model):
    first_name = models.CharField(verbose_name="First Name", max_length=200)
    last_name = models.CharField(verbose_name="Last Name", max_length=200)
    birthday = models.DateField(verbose_name="Birthday", null=True)
    country = models.ForeignKey(Country, on_delete=models.SET_NULL, null=True)
    photo = models.ImageField(upload_to="images/directors", blank=True, null=True)
    biography = models.TextField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Movie(models.Model):
    title = models.CharField(verbose_name="Title", max_length=200)
    year = models.IntegerField(verbose_name="Year")

    photo = models.ImageField(upload_to="images/movies", blank=True, null=True)
    screenshot1 = models.ImageField(upload_to="images/screenshots", blank=True, null=True)
    screenshot2 = models.ImageField(upload_to="images/screenshots", blank=True, null=True)
    screenshot3 = models.ImageField(upload_to="images/screenshots", blank=True, null=True)

    genre = models.ManyToManyField(Genre, related_name="movies")
    country = models.ManyToManyField(Country, related_name="movies")
    director = models.ManyToManyField(Director, related_name="movies", null=True)
    actors = models.ManyToManyField(Actor, related_name="movies")

    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)

    rating = models.DecimalField(max_digits=3, decimal_places=1, blank=True, null=True)
    imdb_rating = models.DecimalField(
        max_digits=3, decimal_places=1, blank=True, null=True
    )
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.title} ({self.year})"


class Comments(models.Model):
    text = models.TextField()

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    movie = models.ForeignKey(Movie, on_delete=models.SET_NULL, null=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.text
