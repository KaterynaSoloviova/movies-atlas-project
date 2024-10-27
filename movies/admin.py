from django.contrib import admin

# Register your models here.
from .models import Movie, Genre, Category, Actor, Director, Country

admin.site.register(Movie)
admin.site.register(Genre)
admin.site.register(Category)
admin.site.register(Actor)
admin.site.register(Director)
admin.site.register(Country)
