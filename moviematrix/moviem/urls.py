from django.contrib import admin
from django.urls import path, include
from . import views
from django.contrib.auth import views as auth_views
from .views import register, user_login

urlpatterns = [
    path('', views.base, name='base'),
    path('movie_list/<int:genre_id>', views.movie_list, name='movie_list'),
    path('movie_details/<int:movie_id>', views.movie_details, name='movie_details'),
    path('cast_list/<int:movie_id>', views.cast_list, name='cast_list'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('register/', register, name='register'),
    path('login/', user_login, name='login'),
]

