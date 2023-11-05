import requests
from django.shortcuts import render
from .models import Movie, Director, Actor, Genre


def fetch_movie_data(request):
    url = "https://api.themoviedb.org/3/movie/550?api_key=239e8e686b9eef955b92516a351c9286"
    response = requests.get(url)
    print(response.text)
    if response.status_code == 200:
        movie_data = response.json()
        results = movie_data.get("results", {"results": "No results"})

        if results:
            for movie_info in movie_data:
                title = movie_info.get('original_title')
                release_date = movie_info.get('release_date')
                genres = [genre['name'] for genre in movie_data.get('genres', [])]
    return render(request, 'movies/movie_list.html', {'message': 'Movie data fetched successfully!'})


def actors_data(request):
    url = "https://api.themoviedb.org/3/movie/movie_id/credits?api_key=239e8e686b9eef955b92516a351c9286"
    response = requests.get(url)
    print(response.text)
    if response.status.code == 200:
        actors = response.json()
        results = actors.get("results", {"results": "No results"})

        if results:
            for actors_info in actors:
                name = actors_info.get("name")
                actor_gender = "Male" if actors_info.get("gender") == 2 else "Female"

