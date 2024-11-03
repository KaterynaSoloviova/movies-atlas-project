from django.urls import path
from . import views

app_name = "movies"
urlpatterns = [
    path("movies/", views.movie_list, name="movie_list"),
    path("movies/<int:pk>/", views.get_movie, name="get_movie"),
    path("actors/<int:pk>/", views.get_actor, name="get_actor"),
    path("director/<int:pk>/", views.get_director, name="get_director"),
]
