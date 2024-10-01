from rest_framework import permissions, viewsets, generics
from core.models.movie import Movie
from api.serializers.movie import MovieStorageSerializer
from api.pagination import StandardResultsSetPagination

class MoviePopularList(generics.ListAPIView):
    """
    API endpoint that show a list of the 20 most popular movies, sorted by popularity
    """
    queryset = Movie.objects.all().order_by('-popularity')
    serializer_class = MovieStorageSerializer
    permission_classes = [permissions.AllowAny, ]
    pagination_class = StandardResultsSetPagination
    
    
class MovieViewSet(viewsets.ModelViewSet):
    """
    API endpoint that:
    * Display details of a specific Movie based on its ID
    * Create a new Movi object
    * Update the Movie objetct
    """
    queryset = Movie.objects.all()
    serializer_class = MovieStorageSerializer
    permission_classes = [permissions.AllowAny, ]
    pagination_class = StandardResultsSetPagination