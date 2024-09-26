from django.db import models

class Genre(models.Model):
    name = models.CharField(max_length=60)
    
    class Meta:
        db_table = 'genre'
