import requests
from django.shortcuts import render
from .models import Movie, Director, Actor, Genre


def fetch_movie_data(request):
    api_key = '239e8e686b9eef955b92516a351c9286'
    movie_id = 550
    url = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key={api_key}"
    response = requests.get(url)
    print(response.text)

    if response.status_code == 200:
        movie_data = response.json()

        for movie_info in movie_data:
            title = movie_info.get('original_title')
            release_date = movie_info.get('release_date')
            genres = [genre['name'] for genre in movie_data.get('genres', [])]

        return render(request, 'movies/movie_list.html', {
            'title': title,
            'release_date': release_date,
            'genres': genres
        })
    else:
        return render(request, 'movies/movie_list.html', {'message': 'Error fetching movie data'})


def actors_data(request):
    api_key = '239e8e686b9eef955b92516a351c9286'
    movie_id = 550
    url = f"https://api.themoviedb.org/3/movie/{movie_id}api_key={api_key}"
    response = requests.get(url)
    print(response.text)

    if response.status.code == 200:
        actors = response.json()
        results = actors.get("results", {"results": "No results"})

        if results:
            for actors_info in actors:
                name = actors_info.get("name")
                actor_gender = "Male" if actors_info.get("gender") == 2 else "Female"
