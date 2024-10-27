from django.shortcuts import render
from django.http import HttpRequest, HttpResponse

from movies.models import Movie


def movie_list(request: HttpRequest) -> HttpResponse:
    movies = Movie.objects.all()
    return render(request, "movies/index.html", {"movies": movies})
