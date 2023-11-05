import requests
from django.shortcuts import render

from moviematrix.api import fetch_data


def homepage(request):
    results = fetch_data()

    if results.status_code == 200:
        movie_data = results.json()
       # for movie in results:
            #new_movie = Movie(
               # title=movie.get('title')
                #release_date=movie.get('release_date')
                #other attributes
           # )
            #new_movie.save()
        title = movie_data.get('original_title')
        release_date = movie_data.get('release_date')
        genres = movie_data.get('genres', [])[0].get('name')

        return render(request, 'movies/movie_list.html', {
            'title': title,
            'release_date': release_date,
            'genres': genres
        })
    else:
        return render(
            request, 'movies/movie_list.html',
            {'message': 'Error fetching movie data'}
        )


def actors_data(request):
    api_key = '239e8e686b9eef955b92516a351c9286'
    movie_id = 550
    url = f"https://api.themoviedb.org/3/movie/{movie_id}api_key={api_key}"
    response = requests.get(url)

    if response.status_code == 200:
        actors = response.json()
        results = actors.get("results", {"results": "No results"})

        if results:
            for actors_info in actors:
                name = actors_info.get("name")
                actor_gender = "Male" if actors_info.get("gender") == 2 else "Female"

    else:
        return render(
            request, 'movies/movie_list.html',
            {'message': 'Error fetching actors data'}
        )
