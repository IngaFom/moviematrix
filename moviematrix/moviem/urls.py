
from django.contrib.auth import views as auth_views
from django.urls import path

from . import views
from .views import register, user_login, movie_search, all_movies, all_genres, single_movie, single_genre

urlpatterns = [
    path('', views.base, name='base'),
    path('movie_list/<int:genre_id>', views.movie_list, name='movie_list'),
    path('movie_details/<int:movie_id>', views.movie_details, name='movie_details'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('register/', register, name='register'),
    path('login/', user_login, name='login'),
    path('search/', movie_search, name='movie_search'),
    path('all_movies/', all_movies, name='all_movies'),
    path('all_genres/', all_genres, name='all_genres'),
    path('movie/<int:movie_id>/', single_movie, name='single_movie'),
    path('genre/<int:genre_id>/', single_genre, name='single_genre'),
]

