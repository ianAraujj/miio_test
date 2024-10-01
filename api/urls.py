from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from api.views import MoviePopularList, MovieViewSet

urlpatterns = [
    path('movie/', MovieViewSet.as_view({'post': 'create'}), name='movie-create'),
    path('movie/<int:pk>/', MovieViewSet.as_view({'get': 'retrieve', 'put': 'update'}), name='movie-read-update'),
    path('movie/popular', MoviePopularList.as_view(), name='movie-popular')
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)