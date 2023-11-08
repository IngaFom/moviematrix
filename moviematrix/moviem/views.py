import requests
from django.shortcuts import render
from moviematrix import fetch_data
from .models import Movie, Director, Actor, Genre


def homepage(request):
    api_key = '239e8e686b9eef955b92516a351c9286'
    movie_id = 550
    url = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key={api_key}"
    response = requests.get(url)

    if response.status_code == 200:
        movie_data = response.json()
        title = movie_data.get('original_title')
        release_date = movie_data.get('release_date')
        genres = "all_genres"

        return render(request, 'base.html', {
            'title': title,
            'release_date': release_date,
            'genres': genres
        })

    return render(request, 'base.html',
                  {'message': 'Error fetching movie data'})


def movie_list(request):
    results = fetch_data()

    if results.status_code == 200:
        movie_data = results.json()
        titles = []
        release_dates = []
        all_genres = []

        for movie in movie_data.get('results', []):
            title = movie.get('original_title')
            release_date = movie.get('release_date')
            genres = [genre['name'] for genre in movie.get('genres', [])]
            titles.append(title)
            release_dates.append(release_date)
            all_genres.append(genres)

        return render(request, 'movies/movie_list.html', {
            'titles': titles,
            'release_dates': release_dates,
            'genres_list': all_genres
        })

    return render(request, 'movies/movie_list.html',
                  {'message': 'Error fetching movie data'})


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
