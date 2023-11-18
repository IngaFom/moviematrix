import requests
from django.conf import settings


def fetch_api(request_type, **kwargs):
    api_key = settings.API_KEY
    base_url = "https://api.themoviedb.org/3/"

    endpoints = {
        "genre": "genre/movie/list",
        "movie_list": "movie/popular",
        "movie_details": "movie/{movie_id}",
        "actors_data": "movie/{movie_id}/credits",
        "search": "search/movie"
    }

    endpoint_url = endpoints.get(request_type, "")
    if not endpoint_url:
        raise ValueError(f"Invalid request_type: {request_type}")

    url = f"{base_url}{endpoint_url}?language=en-US&api_key={api_key}"

    if "{movie_id}" in endpoint_url and 'movie_id' in kwargs:
        url = url.format(movie_id=kwargs['movie_id'])

    if 'page' in kwargs:
        url += f"&page={kwargs['page']}"

    if 'query' in kwargs:
        url += f"&query={kwargs['query']}"

    try:
        response = requests.get(url)
        response.raise_for_status()
        return response
    except requests.RequestException as e:
        print(f"Request failed: {e}")
        return {}
