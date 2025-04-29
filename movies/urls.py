from django.urls import path
from .views import MovieListCreate, MovieDetail

urlpatterns = [
    path('filmes/', MovieListCreate.as_view(), name='movie-list-create'),
    path('filmes/<int:pk>/', MovieDetail.as_view(), name='movie-detail'),
]
