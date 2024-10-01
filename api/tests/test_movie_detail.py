from rest_framework.test import APITestCase
from django.urls import reverse
from core.models.movie import Movie
from api.tests.factories import MovieFactory

class MovieDetailTest(APITestCase):
    def setUp(self):
        self.movie = MovieFactory()
        
    def test_get_movie_detail_status_code(self):
        url = reverse('movie-read-update', kwargs={'pk': self.movie.id})
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        
    def test_get_movie_detail_id(self):
        url = reverse('movie-read-update', kwargs={'pk': self.movie.id})
        response = self.client.get(url)
        self.assertEqual(response.data['id'], self.movie.id)
        
    def test_get_movie_detail_title(self):
        url = reverse('movie-read-update', kwargs={'pk': self.movie.id})
        response = self.client.get(url)
        self.assertEqual(response.data['title'], self.movie.title)
        
    def test_get_movie_detail_genres_ids(self):
        url = reverse('movie-read-update', kwargs={'pk': self.movie.id})
        response = self.client.get(url)
        self.assertEqual(True if 'genre_ids' in response.data else False, True)
        
    def test_get_movie_detail_genres_ids_count(self):
        url = reverse('movie-read-update', kwargs={'pk': self.movie.id})
        response = self.client.get(url)
        self.assertEqual(len(response.data.pop('genre_ids', [])), self.movie.genres.count())