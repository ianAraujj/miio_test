from rest_framework.test import APITestCase
from django.urls import reverse
from api.tests.factories import MovieFactory, GenreFactory, generate_image_base_64
from core.models.movie import Movie
import random
import factory
import base64

class MovieCreateTest(APITestCase):
    def setUp(self):
        # Generate GENRES
        self.genres = list(
            GenreFactory.create_batch(random.randint(3, 7))
        )
        
        # BUILD FUNCTION creates the object in memory without saving
        self.movie = factory.build(dict, FACTORY_CLASS=MovieFactory)
        
        # DEFINE GENRES
        self.movie['genre_ids'] = [genre.id for genre in self.genres]
        
        
    def test_create_movie_sucess_status_code(self):
        url = reverse('movie-create')
        data = self.movie
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, 201)
        
    def test_create_movie_sucess(self):
        url = reverse('movie-create')
        data = self.movie
        response = self.client.post(url, data, format='json')
        self.assertEqual(
            Movie.objects.filter(id=response.json().get('id')).count(), 1
        )
        
    def test_create_movie_genres(self):
        url = reverse('movie-create')
        data = self.movie
        response = self.client.post(url, data, format='json')
        movie_created = Movie.objects.get(id=response.json().get('id'))
        self.assertEqual(
            movie_created.genres.all().count(),
            len(data['genre_ids'])
        )
        self.assertEqual(
            movie_created.genres.first().id,
            data['genre_ids'][0]
        )
        
    def test_create_movie_popularity(self):
        url = reverse('movie-create')
        data = self.movie
        response = self.client.post(url, data, format='json')
        movie_created = Movie.objects.get(id=response.json().get('id'))
        self.assertEqual(movie_created.popularity, data['popularity'])
        
    def test_create_movie_vote_count(self):
        url = reverse('movie-create')
        data = self.movie
        response = self.client.post(url, data, format='json')
        movie_created = Movie.objects.get(id=response.json().get('id'))
        self.assertEqual(movie_created.vote_count, data['vote_count'])
        
    def test_create_movie_vote_count_fail(self):
        url = reverse('movie-create')
        data = self.movie
        data['vote_count'] = data['vote_count'] * -1
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json(), {'vote_count': ['Ensure this value is greater than or equal to 0.']})
        
    def test_create_movie_poster_path_save(self):
        url = reverse('movie-create')
        data = self.movie
        data['poster_path_base64'] = generate_image_base_64()
        response = self.client.post(url, data, format='json')
        movie_created = Movie.objects.get(id=response.json().get('id'))        
        self.assertEqual(True if movie_created.poster_path else False, True)
        
    def test_create_movie_poster_path_check_file(self):
        url = reverse('movie-create')
        data = self.movie
        data['poster_path_base64'] = generate_image_base_64()
        response = self.client.post(url, data, format='json')
        movie_created = Movie.objects.get(id=response.json().get('id'))
        
        # Image Saved
        with open(movie_created.poster_path.path, 'rb') as saved_file:
            saved_image_data = saved_file.read()
            
        # Image Sent
        image_sent = base64.b64decode(data['poster_path_base64'].split(',')[1])
        
        self.assertEqual(saved_image_data, image_sent)
