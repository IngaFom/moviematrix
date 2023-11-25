from django.test import TestCase
from django.urls import reverse
from unittest.mock import patch, Mock
from django.conf import settings
from .api import fetch_api
from .forms import CustomUserCreationForm


class Tests(TestCase):

    def test_custom_user_creation_form(self):
        data = {
            'username': 'testuser',
            'password1': 'testpassword123',
            'password2': 'testpassword123',
            'email': 'testuser@example.com',
        }
        form = CustomUserCreationForm(data)

        if form.is_valid():
            print("Test passed: Form is valid.")
        else:
            print(f"Test failed: Form is not valid. Errors: {form.errors}")

        self.assertTrue(form.is_valid())

    def test_movie_search_view(self):
        with (patch('moviem.views.fetch_api') as mock_fetch_api):
            mock_fetch_api.return_value.status_code = 200
            mock_fetch_api.return_value.json.return_value = {'results':
                                                                 [{'id': 1,
                                                                   'title':
                                                                       'Test Movie'
                                                                   }]}

            response = self.client.get(reverse('movie_search'), {'q': 'test'})

            self.assertEqual(response.status_code, 200)
            self.assertTemplateUsed(response, 'movies/search_results.html')
            self.assertIn('results', response.context)
            self.assertIn('query', response.context)

            expected_message = " Search view test passed successfully." if 'results' in response.context \
                                                              and 'query' in response.context \
                else "Test failed: Unexpected response."
            print(expected_message)

    def test_database_engine(self):
        expected_engine = 'django.db.backends.mysql'
        actual_engine = settings.DATABASES['default']['ENGINE']

        if actual_engine == expected_engine:
            print(f"Test passed successfully: Expected database engine is {expected_engine}.")
        else:
            print(f"Test failed: Unexpected database engine. Expected: {expected_engine}, Got: {actual_engine}")

        self.assertEqual(actual_engine, expected_engine)

    @patch('moviem.api.requests.get')
    def test_api_key(self, mock_get):

        mock_response = Mock()
        mock_response.status_code = 200
        mock_get.return_value = mock_response

        response = fetch_api(request_type='genre')
        mock_get.assert_called_once_with(
            f'https://api.themoviedb.org/3/genre/movie/list?language=en-US&api_key={settings.API_KEY}'
        )
        self.assertEqual(response.status_code, 200)

        if response.status_code == 200:
            print("Api works")
        else:
            print("API dont work")
