import requests
from random import sample
from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required

from .api import fetch_movie_list, fetch_genre_list, fetch_movie_details, fetch_actors_data
from .forms import CustomUserCreationForm
from .models import Movie, Director, Actor, Genre


def base(request):
    results = fetch_genre_list()
    movie_results = fetch_movie_list()

    if results.status_code == 200 and movie_results.status_code == 200:
        genre_data = results.json()
        movie_data = movie_results.json().get('results', [])
        random_posters = sample(movie_data, 5)

        return render(request, 'homepage/base.html', {
            'base': genre_data.get('genres', []),
            'random_posters': random_posters
        })

    return render(request, 'homepage/base.html',
                  {'message': 'Error fetching genre data'})


def movie_list(request, genre_id):
    all_movies = []

    for page_number in range(1, 10):
        results = fetch_movie_list(page=page_number)

        if results.status_code == 200:
            movie_data = results.json().get('results', [])

            filtered_movies = [movie for movie in movie_data if genre_id in movie.get('genre_ids', [])]

            all_movies.extend(filtered_movies)

    return render(request, 'movies/movie_list.html', {'movie_list_data': all_movies})


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

        actors_data = fetch_actors_data(movie_id)

        if actors_data.status_code == 200:
            actors = actors_data.json().get('cast', [])

            return render(request, 'movies/movie_details.html', {
                'movie_data': movie_data,
                'actors': actors
            })

    return render(request, 'movies/movie_details.html', {'message': 'Error fetching movie details'})


def register(request):
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("profile")
    else:
        form = CustomUserCreationForm()
    return render(request, "movies/registration/registration_form.html", {"form": form})


@login_required
def profile(request):
    return render(request, 'homepage/base.html')


def user_login(request):
    if request.method == "POST":
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('profile')
    else:
        form = AuthenticationForm()
    return render(request, 'homepage/login.html', {'form': form})

