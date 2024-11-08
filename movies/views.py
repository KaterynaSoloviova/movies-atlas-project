from django.http import HttpRequest, HttpResponse
from django.shortcuts import get_object_or_404, render
from movies.models import Movie, Actor, Director, Country, Genre, Category


def movie_list(request: HttpRequest) -> HttpResponse:
    country_list = Country.objects.all()
    genre_list = Genre.objects.all()
    category_list = Category.objects.all()

    movies_list = Movie.objects.all()

    country_id = request.GET.get("country")
    selected_country_id = -1
    if country_id is not None and country_id != "-1":
        movies_list = movies_list.filter(country=country_id)
        selected_country_id = int(country_id)

    genre_id = request.GET.get("genre")
    selected_genre_id = -1
    if genre_id is not None and genre_id != "-1":
        movies_list = movies_list.filter(genre=genre_id)
        selected_genre_id = int(genre_id)

    year_from = request.GET.get("year_from")
    selected_year_from = 1930
    if year_from is not None:
        selected_year_from = int(year_from)
        movies_list = movies_list.filter(year__gte=selected_year_from)

    year_to = request.GET.get("year_to")
    selected_year_to = 2025
    if year_to is not None:
        selected_year_to = int(year_to)
        movies_list = movies_list.filter(year__lte=selected_year_to)

    category_ids = []
    for category in category_list:
        if request.GET.get(category.name) is not None:
            category_ids.append(category.id)
    if len(category_ids) != 0:
        movies_list = movies_list.filter(category__in=category_ids)

    rating = request.GET.get("rating")
    selected_rating_imdb = 1
    if rating is not None:
        selected_rating_imdb = float(rating)
        movies_list = movies_list.filter(imdb_rating__gte=selected_rating_imdb)

    return render(request, "movies/index.html",
                  {"movies_list": movies_list, "country_list": country_list, "genre_list": genre_list,
                   "category_list": category_list, "category_ids": category_ids,
                   "selected_country_id": selected_country_id, "selected_genre_id": selected_genre_id,
                   "selected_year_from": selected_year_from, "selected_year_to": selected_year_to,
                   "selected_rating_imdb": selected_rating_imdb})


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
