from django.urls import path
from .views import MovieList, AllMovies


urlpatterns = [
    path('all/', AllMovies.as_view(), name='allmoives'),
    path('<slug>/', MovieList.as_view(), name='moives'),
]