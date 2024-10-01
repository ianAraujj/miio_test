from rest_framework import serializers
from api.mixin import Base64FileField
from core.models.movie import Movie
from core.models.genre import Genre

class MovieStorageSerializer(serializers.ModelSerializer):
    genre_ids = serializers.PrimaryKeyRelatedField(queryset=Genre.objects.all(), many=True, source='genres')
    backdrop_path_base64 = Base64FileField(required=False, write_only=True, source='backdrop_path')
    poster_path_base64 = Base64FileField(required=False, write_only=True, source='poster_path')
    
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
            'backdrop_path_base64',
            'poster_path',
            'poster_path_base64',
            'genre_ids'
        ]
        extra_kwargs = {
            'id': {'read_only': False, 'required': False},
            'genres': {'required': False, 'write_only': True, 'allow_empty': True}
        }
        
    def storage(self, validated_data):
        instance = Movie.objects.filter(id=validated_data['id']).last()
        return self.update(instance, validated_data) if instance else self.create(validated_data)