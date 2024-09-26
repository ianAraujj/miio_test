from django.core.files.base import ContentFile
from data_consumption.tmdb import TMDB
from core.models.genre import Genre
from api.serializers.movie import MovieStorageSerializer
from decouple import config

class StorageMovie(object):
    """
    Class created to store movie information in the database
    """
    
    def __init__(self):
        if not config('TMDB_API_ACESS_TOKEN', None):
            raise ValueError("Configure TMDB API Credentials")
        
        self.api_movie = TMDB(config('TMDB_API_ACESS_TOKEN'))
        self.resolution_file_image = 'w300'
        self.fields_file = ['backdrop_path', 'poster_path']
    
    def storage_movie_genres(self):
        """
        function to consult and save movie genres
        """
        resp_api = self.api_movie.list_genres()
        if resp_api and 'genres' in resp_api:
            for resp in resp_api['genres']:
                Genre.objects.get_or_create(**resp)
    
    def storage_movie_data(self):
        """
        function to consult and save movies in the system
        """
        # Salve Genres
        self.storage_movie_genres()
        
        # Salve Movies
        resp_api = self.api_movie.list_popular_movies()
        if resp_api and 'results' in resp_api:
            for resp in resp_api['results']:
                
                # Download Files
                for field in self.fields_file:
                    if field in resp:
                        file = self.api_movie.download_file(resp[field], self.resolution_file_image)
                        if file:
                            resp[field] = ContentFile(file, name=resp[field].replace('/', ''))
            
            movie_serializer = MovieStorageSerializer(data=resp_api['results'], many=True)
            movie_serializer.is_valid(raise_exception=True)
            #movie_serializer.storage()
            for validated_data in movie_serializer.validated_data:
                MovieStorageSerializer().storage(validated_data)