from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.genre_list, name='genre_list'),
    path('movie_list/<int:genre_id>', views.movie_list, name='movie_list'),
    path('movie_details/<int:movie_id>', views.movie_details, name='movie_details'),
]