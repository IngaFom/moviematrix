from random import sample
from django.shortcuts import render
from django.contrib.auth.forms import AuthenticationForm, PasswordResetForm
from django.contrib.auth.tokens import default_token_generator
from django.contrib.auth import login, get_user_model
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from .api import fetch_api
from .forms import CustomUserCreationForm
from .models import UserProfile, Genre
from django.contrib.auth.views import PasswordResetView, PasswordResetDoneView, PasswordResetConfirmView, PasswordResetCompleteView
from django.urls import reverse_lazy
from django.template.response import TemplateResponse


def custom_password_reset(request):
    if request.method == "POST":
        form = PasswordResetForm(request.POST)
        if form.is_valid():
            UserModel = get_user_model()
            email = form.cleaned_data["email"]
            users = UserModel._default_manager.filter(email__iexact=email)
            if users.exists():
                for user in users:
                    context = {
                        'email': user.email,
                        'domain': request.get_host(),
                        'site_name': 'Your Site',
                        'uid': default_token_generator.make_token(user),
                        'user': user,
                        'protocol': 'http',
                    }
                    subject_template_name = 'registration/password_reset_subject.txt'
                    # Create your own email body template
                    email_template_name = 'registration/custom_password_reset_email.html'
                    return TemplateResponse(request, email_template_name, context)
    else:
        form = PasswordResetForm()
    return render(request, 'registration/custom_password_reset_form.html', {'form': form})


class CustomPasswordResetView(PasswordResetView):
    template_name = 'registration/custom_password_reset_form.html'
    email_template_name = 'moviematrix/moviem/templates/password_reset_email.html'
    success_url = reverse_lazy('password_reset_done')

class CustomPasswordResetDoneView(PasswordResetDoneView):
    template_name = 'registration/custom_password_reset_done.html'

class CustomPasswordResetConfirmView(PasswordResetConfirmView):
    template_name = 'registration/custom_password_reset_confirm.html'
    success_url = reverse_lazy('password_reset_complete')

class CustomPasswordResetCompleteView(PasswordResetCompleteView):
    template_name = 'registration/custom_password_reset_complete.html'


def profile(request):
    user_profile = UserProfile.objects.get(
        user=request.user
    )

    return render(
        request,
        '../templates/movies/registration/profile.html',
        {'user_profile': user_profile},
    )


def base(request):
    genre_data = {}
    random_posters = []
    results = fetch_api(request_type="genre")

    all_movies = []
    for page_number in range(1, 10):
        movie_results = fetch_api(
            request_type="movie_list",
            page=page_number
        )
        if movie_results.status_code == 200:
            movie_data = movie_results.json().get(
                'results', []
            )

            all_movies.extend(movie_data)

        if results.status_code == 200:
            genre_data = results.json()
            random_posters = sample(all_movies, 20)

        return render(request,
                      'homepage/base.html',
                      {
                          'base': genre_data.get('genres', {}),
                          'random_posters': random_posters
                      })

    return render(request, 'homepage/base.html',
                  {'message': 'Error fetching genre data'}
                  )


def movie_search(request):
    query = request.GET.get('q', '')

    if query:
        search_results = fetch_api(request_type="search",
                                   query=query
                                   )

        if search_results.status_code == 200:
            search_data = (search_results.json().get
                           ('results', [])
                           )

            return render(
                request,
                'movies/search_results.html',
                {'results': search_data,
                 'query': query}
            )

    return render(
        request, 'movies/search_results.html',
        {'message': 'No results found',
         'query': query}
    )


def movie_list(request, genre_id):
    all_movies = []

    for page_number in range(1, 10):
        results = fetch_api(request_type="movie_list",
                            page=page_number
                            )

        if results.status_code == 200:
            movie_data = results.json().get('results', [])

            filtered_movies = [movie
                               for movie in movie_data
                               if genre_id in movie.get('genre_ids',
                                                        [])
                               ]

            all_movies.extend(filtered_movies)

    return render(
        request,
        'movies/movie_list.html',
        {'movie_list_data': all_movies}
    )


def all_categories(request):
    genres = Genre.objects.all()
    return render(request, 'movies/movie_list.html', {'genre': genres})


def movie_details(request, movie_id):
    movie_details_response = fetch_api(
        request_type="movie_details",
        movie_id=movie_id
    )

    if movie_details_response.status_code == 200:
        movie_data = movie_details_response.json()

        actors_data = fetch_api(
            request_type="actors_data",
            movie_id=movie_id
        )

        if actors_data.status_code == 200:
            actors = actors_data.json().get('cast', [])

            return render(
                request,
                'movies/movie_details.html',
                {
                    'movie_data': movie_data,
                    'actors': actors
                }
            )


def register(request):
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("profile")
    else:
        form = CustomUserCreationForm()
    return render(
        request,
        "movies/registration/registration_form.html",
        {"form": form}
    )


@login_required
def profile(request):
    return render(request, 'homepage/base.html')


def user_login(request):
    if request.method == "POST":
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('profile')
    else:
        form = AuthenticationForm()
    return render(
        request,
        'registration/login.html',
        {'form': form}
    )


@login_required(login_url='http://127.0.0.1:8000/login/')
def profile_view(request):
    return render(request, 'movies/registration/profile.html')
