from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.core import serializers
from django.shortcuts import get_object_or_404
from django.forms.models import model_to_dict
from cinema.models import Genre, Movie, Artist
from first_example.helpers.model_helper import ModelHelper
import json


def index(request):
    a = {
        'message': 'hola'
    }
    return JsonResponse(a, status=200)


def movie(request):
    if request.method == 'GET':
        response = ModelHelper.retrieveAll(Movie)
    elif request.method == 'POST':
        a = {
            'message': 'hiciste post perro :\'v'
        }
    return JsonResponse(a, status=200)

def genre(request, genre_id=0):
    if request.method == 'GET':
        response = ModelHelper.retrieveAll(Genre)
    elif request.method == 'POST':
        received_data = json.loads(request.body)
        genre = Genre(name=received_data["name"])
        genre.save()
        response = {
            'success': True,
            'data': genre.__str__()
        }
    elif request.method == 'PUT':
        received_data = json.loads(request.body)
        genre = get_object_or_404(Genre, pk=genre_id)
        genre.name = received_data["name"]
        genre.save()
        response = {
            'success': True,
            'updated': model_to_dict(genre)
        }
    return JsonResponse(response, status=200)
