from rest_framework import serializers
from core.models.movie import Movie
from core.models.genre import Genre

class MovieStorageSerializer(serializers.ModelSerializer):
    genre_ids = serializers.PrimaryKeyRelatedField(queryset=Genre.objects.all(), many=True, source='genres')
    
    class Meta:
        model = Movie
        fields = [
            'id',
            'adult', 
            'original_language', 
            'original_title', 
            'title', 
            'overview', 
            'release_date', 
            'genres', 
            'popularity', 
            'vote_average', 
            'vote_count', 
            'backdrop_path', 
            'poster_path',
            'genre_ids'
        ]
        extra_kwargs = {
            'id': {'read_only': False},
            'genres': {'required': False}
        }
        
    def storage(self, validated_data):
        instance = Movie.objects.filter(id=validated_data['id']).last()
        return self.update(instance, validated_data) if instance else self.create(validated_data)