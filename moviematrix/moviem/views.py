import requests
from random import sample
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required

from .api import fetch_movie_list, fetch_genre_list, fetch_movie_details, fetch_actors_data
from .forms import CustomUserCreationForm
from .models import Movie, Director, Actor, Genre


def search_tmdb(query):
    api_key = '239e8e686b9eef955b92516a351c9286'
    base_url = 'https://api.themoviedb.org/3/search/movie'
    params = {
        'api_key': api_key,
        'query': query,
    }
    response = requests.get(base_url, params=params)
    data = response.json()
    return data.get('results', [])


def base(request):
    results = fetch_genre_list()

    for page_number in range(1, 10):
        movie_results = fetch_movie_list(page=page_number)

    if results.status_code == 200 and movie_results.status_code == 200:
        genre_data = results.json()
        movie_data = movie_results.json().get('results', [])
        random_posters = sample(movie_data, 20)

        return render(request, 'homepage/base.html', {
            'base': genre_data.get('genres', []),
            'random_posters': random_posters
        })

    return render(request, 'homepage/base.html',
                  {'message': 'Error fetching genre data'})


def movie_search(request):
    query = request.GET.get('q', '')

    if query:

        search_results = search_tmdb(query)

        if search_results:
            return render(request, 'movies/search_results.html', {'results': search_results, 'query': query})

    return render(request, 'movies/search_results.html', {'message': 'No results found', 'query': query})


def all_movies(request):
    movies = Movie.objects.all()
    return render(request, 'movies/all_movies.html', {'movies': movies})


def all_genres(request):
    genres = Genre.objects.all()
    return render(request, 'movies/all_genres.html', {'genres': genres})


def single_movie(request, movie_id):
    movie = get_object_or_404(Movie, id=movie_id)
    return render(request, 'movies/single_movie.html', {'movie': movie})


def single_genre(request, genre_id):
    genre = get_object_or_404(Genre, id=genre_id)
    return render(request, 'movies/single_genre.html', {'genre': genre})


def movie_list(request, genre_id):
    all_movies = []

    for page_number in range(1, 10):
        results = fetch_movie_list(page=page_number)

        if results.status_code == 200:
            movie_data = results.json().get('results', [])

            filtered_movies = [movie for movie in movie_data if genre_id in movie.get('genre_ids', [])]

            all_movies.extend(filtered_movies)

    return render(request, 'movies/movie_list.html', {'movie_list_data': all_movies})


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
