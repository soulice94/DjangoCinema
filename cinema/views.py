from django.shortcuts import render, get_object_or_404, get_list_or_404
from django.http import HttpResponse, JsonResponse
from django.core import serializers
from django.db.models import Q
from django.forms.models import model_to_dict
from cinema.models import Genre, Movie, Artist
from first_example.helpers.model_helper import ModelHelper
import constants
import json


def index(request):
    a = {
        'message': 'hola'
    }
    return JsonResponse(a, status=200)

def artist(request, artist_id=0):
    if ModelHelper.need_json_body(request.method):
        received_data = json.loads(request.body)
    if request.method == constants.GET_METHOD:
        response = ModelHelper.retrieve_all(Artist)
    elif request.method == constants.POST_METHOD:
        artist = Artist.objects.create(
            name=received_data["name"],
            last_name=received_data["last_name"]
        )
        response = {
            'success': True,
            'created': model_to_dict(artist)
        }
    elif request.method == constants.PUT_METHOD:
        received_data = json.loads(request.body)
        artist = get_object_or_404(Artist, pk=artist_id)
        artist.name = received_data["name"]
        artist.last_name = received_data["last_name"]
        artist.save()
        response = {
            'success': True,
            'updated': model_to_dict(artist)
        }
    elif request.method == constants.DELETE_METHOD:
        artist = get_object_or_404(Artist, pk=artist_id)
        artist_data = model_to_dict(artist)
        artist.delete()
        response = {
            'success': True,
            'deleted': artist_data
        }
    return JsonResponse(response, status=200)


def movie(request, movie_id=0):
    if ModelHelper.need_json_body(request.method):
        received_data = json.loads(request.body)
    if request.method == constants.GET_METHOD:
        response = ModelHelper.retrieve_movie_list(Movie.objects.all())
    elif request.method == constants.POST_METHOD:
        genre = get_object_or_404(Genre, pk=received_data["genre"])
        actors_list = get_list_or_404(Artist, pk__in=received_data["actors"])
        movie = Movie.objects.create(
            name=received_data["name"],
            genre=genre
        )
        movie.actors.set(actors_list)
        response = {
            'success': True,
            'created': ModelHelper.movie_serializer(movie)
        }
    elif request.method == constants.PUT_METHOD:
        movie = get_object_or_404(Movie, pk=movie_id)
        genre = get_object_or_404(Genre, pk=received_data["genre"])
        movie.name = received_data["name"]
        movie.genre = genre
        movie.save()
        response = {
            'success': True,
            'updated': ModelHelper.movie_serializer(movie)
        }
    elif request.method == constants.DELETE_METHOD:
        movie = get_object_or_404(Movie, pk=movie_id)
        movie_data = ModelHelper.movie_serializer(movie)
        movie.delete()
        response = {
            'success': True,
            'deleted': movie_data
        }
    return JsonResponse(response, status=200)

def genre(request, genre_id=0):
    if ModelHelper.need_json_body(request.method):
        received_data = json.loads(request.body)
    if request.method == constants.GET_METHOD:
        response = ModelHelper.retrieve_all(Genre)
    elif request.method == constants.POST_METHOD:
        genre = Genre.objects.create(name=received_data["name"])
        response = {
            'success': True,
            'created': model_to_dict(genre)
        }
    elif request.method == constants.PUT_METHOD:
        genre = get_object_or_404(Genre, pk=genre_id)
        genre.name = received_data["name"]
        genre.save()
        response = {
            'success': True,
            'updated': model_to_dict(genre)
        }
    elif request.method == constants.DELETE_METHOD:
        genre = get_object_or_404(Genre, pk=genre_id)
        genre_data = model_to_dict(genre)
        genre.delete()
        response = {
            'success': True,
            'deleted': genre_data
        }
    return JsonResponse(response, status=200)

def movieSearch(request, artist_name=None, movie_name=None):
    query = Q()
    if 'artist_name' in request.GET:
        query.add(Q(actors__name=request.GET["artist_name"]), Q.OR)
    if 'movie_name' in request.GET:
        query.add(Q(name=request.GET["movie_name"]), Q.OR)
    result = Movie.objects.filter(query)
    response = ModelHelper.retrieve_movie_list(result)
    return JsonResponse(response, status=200)
