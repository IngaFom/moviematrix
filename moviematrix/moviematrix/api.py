import requests


def fetch_data(movie_list):
    api_key = '239e8e686b9eef955b92516a351c9286'
    url = F"https://api.themoviedb.org/3/movie/popular?language=en-US&page=1&api_key={api_key}"
    response = requests.get(url)
    return response
