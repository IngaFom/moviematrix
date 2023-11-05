import requests


def fetch_data(movie_id=550):
    api_key = '239e8e686b9eef955b92516a351c9286'
    url = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key={api_key}"
    response = requests.get(url)
    return response

