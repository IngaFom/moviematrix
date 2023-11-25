
from django.contrib.auth import views as auth_views
from django.urls import path, include

from . import views
from .views import register, user_login, movie_search, profile_view

urlpatterns = [
    path('', views.base, name='base'),
    path('movie_list/<int:genre_id>', views.movie_list, name='movie_list'),
    path('movie_details/<int:movie_id>', views.movie_details, name='movie_details'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('register/', register, name='register'),
    path('login/', user_login, name='login'),
    path('search/', movie_search, name='movie_search'),
    path('password_reset/', auth_views.PasswordResetView.as_view(), name='password_reset'),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
    path('password_reset/', include('django.contrib.auth.urls')),
    path('profile/', profile_view, name='profile'),
    path('all_categories/', views.all_categories, name='all_categories'),

]
