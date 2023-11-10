import requests
from django.shortcuts import render

from .api import fetch_movie_list, fetch_genre_list, fetch_movie_details
from .models import Movie, Director, Actor, Genre

def genre_list(request):
    results = fetch_genre_list()

    if results.status_code == 200:
        genre_data = results.json()

        return render(request, 'movies/genre_list.html', {
            'genre_list': genre_data.get('genres', [])
        })

    return render(request, 'movies/genre_list.html',
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

def movie_details(request, movie_id):
    movie_details = fetch_movie_details(movie_id)

    if movie_details.status_code == 200:
        movie_data = movie_details.json()
        return render(request, 'movies/movie_details.html', {
            'movie_data': movie_data
        })

    return render(request, 'movies/movie_details.html', {'message': 'Error fetching movie details'})

def actors_data(request):
    api_key = '239e8e686b9eef955b92516a351c9286'
    movie_id = 550
    url = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key={api_key}"
    response = requests.get(url)

    if response.status_code == 200:
        actors = response.json()
        results = actors.get("results", [])

        actors_info = []
        if results:
            for actor in results:
                name = actor.get("name")
                actor_gender = "Male" if actor.get("gender") == 2 else "Female"
                actors_info.append({"name": name, "gender": actor_gender})

            return render(request, 'actors/actors_list.html',
                          {'actors_info': actors_info})

    return render(request, 'actors/actors_list.html',
                  {'message': 'Error fetching actors data'})
