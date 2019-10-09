from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
import json


def index(request):
    a = {
        'message': 'hola'
    }
    return JsonResponse(a, status=200)
# Create your views here.

def movie(request):
    a = {
        'message': 'represento a las muvis jiji'
    }
    return JsonResponse(a, status=200)
