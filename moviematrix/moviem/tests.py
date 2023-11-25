from django.test import TestCase
from django.urls import reverse
from unittest.mock import patch
from django.conf import settings
from .forms import CustomUserCreationForm


class FormsTest(TestCase):
    def test_custom_user_creation_form(self):
        data = {
            'username': 'testuser',
            'password1': 'testpassword123',
            'password2': 'testpassword123',
            'email': 'testuser@example.com',
        }
        form = CustomUserCreationForm(data)
        self.assertTrue(form.is_valid())


class ViewsTests(TestCase):

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


class DatabaseTests(TestCase):

    def test_database_engine(self):
        expected_engine = 'django.db.backends.mysql'
        actual_engine = settings.DATABASES['default']['ENGINE']

        self.assertEqual(actual_engine, expected_engine,
                         f"Expected database engine to be {expected_engine}, but got {actual_engine}.")
