from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('movie/', views.movie, name='movie'),
    path('api/genre/', views.genre, name='genre'),
    path('api/genre/<int:genre_id>', views.genre, name='genre')
]