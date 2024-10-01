from django.db import models
from core.utils.files import normalize_string
from datetime import datetime
import os

def movie_file_directory(instance, filename):
    now = datetime.now()
    return os.path.join(
        "movies", str(now.year), str(now.month), normalize_string(instance.title), filename)

class Movie(models.Model):
    
    # General Info
    adult = models.BooleanField()
    original_language = models.CharField(max_length=6)
    original_title = models.CharField(max_length=150)
    title = models.CharField(max_length=150)
    overview = models.TextField()
    release_date = models.DateField(null=True)
    genres = models.ManyToManyField('Genre', db_table='movie_genre')
    
    # assessment
    popularity = models.DecimalField(max_digits=15, decimal_places=4, default=0)
    vote_average = models.DecimalField(max_digits=15, decimal_places=4, default=0)
    vote_count = models.PositiveIntegerField(default=0)
    
    # Files
    backdrop_path = models.FileField(upload_to=movie_file_directory, null=True, default=None)
    poster_path = models.FileField(upload_to=movie_file_directory, null=True, default=None)
    
    class Meta:
        db_table = 'movie'