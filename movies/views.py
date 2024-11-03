from django.http import HttpRequest, HttpResponse
from django.shortcuts import get_object_or_404, render
from movies.models import Movie, Actor, Director


def movie_list(request: HttpRequest) -> HttpResponse:
    movies_list = Movie.objects.all()

    return render(request, "movies/index.html", {"movies_list": movies_list})


def get_movie(request: HttpRequest, pk: int) -> HttpResponse:
    movie = Movie.objects.get(pk=pk)

    return render(request, "movies/movie.html", {"movie": movie})


def get_actor(request: HttpRequest, pk: int) -> HttpResponse:
    actor = get_object_or_404(Actor, pk=pk)
    movie_id = request.GET.get("movie")
    movie = Movie.objects.get(pk=movie_id)

    return render(request, "movies/actor.html", {"actor": actor, "movie": movie})


def get_director(request: HttpRequest, pk: int) -> HttpResponse:
    director = get_object_or_404(Director, pk=pk)
    movie_id = request.GET.get("movie")
    movie = Movie.objects.get(pk=movie_id)

    return render(request, "movies/director.html", {"director": director, "movie": movie})
