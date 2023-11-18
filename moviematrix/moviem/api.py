import requests
from django.conf import settings


def fetch_api(movie_id=None, request_type=None, page=1):
    api_key = settings.API_KEY
    base_url = "https://api.themoviedb.org/3/"
    endpoints = {
        "genre": f"genre/movie/list?language=en&api_key={api_key}",
        "movie_list": f"popular?language=en-US&page={page}&api_key={api_key}",
        "movie_details": f"movie/{movie_id}?language=en-US&api_key={api_key}",
        "actors_data": f"movie/{movie_id}/credits?api_key={api_key}"
    }
    final_endpoint = base_url + endpoints.get(request_type)
    try:
        r = requests.get(final_endpoint)
        return r
    except requests.RequestException as e:
        print(f"Request failed: {e}")
        return {}


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
