from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.core import serializers
from django.shortcuts import get_object_or_404
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
    if request.method == constants.GET_METHOD:
        response = ModelHelper.retrieveAll(Artist)
    elif request.method == constants.POST_METHOD:
        received_data = json.loads(request.body)
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
        response = {
            'success': True,
            'deleted': artist_data
        }
    return JsonResponse(response, status=200)


def movie(request):
    if request.method == constants.GET_METHOD:
        response = ModelHelper.retrieveAll(Movie)
    elif request.method == constants.POST_METHOD:
        pass
    return JsonResponse(response, status=200)

def genre(request, genre_id=0):
    if request.method == constants.GET_METHOD:
        response = ModelHelper.retrieveAll(Genre)
    elif request.method == constants.POST_METHOD:
        received_data = json.loads(request.body)
        genre = Genre.objects.create(name=received_data["name"])
        response = {
            'success': True,
            'created': model_to_dict(genre)
        }
    elif request.method == constants.PUT_METHOD:
        received_data = json.loads(request.body)
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
