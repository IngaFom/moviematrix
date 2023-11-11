import requests
import random
from django.shortcuts import render

from .api import fetch_movie_list, fetch_genre_list, fetch_movie_details, fetch_actors_data
from .models import Movie, Director, Actor, Genre


def base(request):
    results = fetch_genre_list()

    if results.status_code == 200:
        genre_data = results.json()

        return render(request, 'movies/base.html', {
            'base': genre_data.get('genres', [])
        })

    return render(request, 'movies/base.html',
                  {'message': 'Error fetching genre data'})


def movie_list(request, genre_id):
    results = fetch_movie_list()

    if results.status_code == 200:
        movie_data = results.json()

        filtered_movies = []

        for movie in movie_data.get('results', []):
            if genre_id in movie.get('genre_ids', []):
                filtered_movies.append(movie)

        return render(request, 'movies/movie_list.html', {
            'movie_list_data': filtered_movies
        })

    return render(request, 'movies/movie_list.html',
                  {'message': 'Error fetching movie data'})


def cast_list(request, movie_id):
    cast_list = fetch_actors_data(movie_id)

    if cast_list.status_code == 200:
        actors = cast_list.json().get('cast', [])

        return render(request, 'movies/cast_list.html', {
            'actors': actors
        })

    return render(request, 'movies/cast_list.html', {'message': 'Error fetching actors data'})


def movie_details(request, movie_id):
    movie_details = fetch_movie_details(movie_id)

    if movie_details.status_code == 200:
        movie_data = movie_details.json()

        return render(request, 'movies/movie_details.html', {
            'movie_data': movie_data
        })

    return render(request, 'movies/movie_details.html', {'message': 'Error fetching movie details'})
