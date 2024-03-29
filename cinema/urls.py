from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('api/movies/', views.movie, name='movies'),
    path('api/movies/<int:movie_id>', views.movie, name='movies'),
    path('api/movies/search/', views.movieSearch, name='movies_search'),
    path('api/artists/', views.artist, name='artists'),
    path('api/artists/<int:artist_id>', views.artist, name='artists'),
    path('api/genres/', views.genre, name='genres'),
    path('api/genres/<int:genre_id>', views.genre, name='genres'),
]