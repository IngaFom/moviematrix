import requests


def fetch_genre_list():
    api_key = '239e8e686b9eef955b92516a351c9286'
    url = f"https://api.themoviedb.org/3/genre/movie/list?language=en&api_key={api_key}"
    response = requests.get(url)
    return response


def fetch_movie_list(page=1):
    api_key = '239e8e686b9eef955b92516a351c9286'
    url = f"https://api.themoviedb.org/3/movie/popular?language=en-US&page={page}&api_key={api_key}"
    response = requests.get(url)
    return response


def fetch_movie_details(movie_id):
    api_key = '239e8e686b9eef955b92516a351c9286'
    url = f"https://api.themoviedb.org/3/movie/{movie_id}?language=en-US&api_key={api_key}"
    response = requests.get(url)
    return response

def fetch_actors_data(movie_id):
    api_key = '239e8e686b9eef955b92516a351c9286'
    url = f"https://api.themoviedb.org/3/movie/{movie_id}/credits?api_key={api_key}"
    response = requests.get(url)
    return response