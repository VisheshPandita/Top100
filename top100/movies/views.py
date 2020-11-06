from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .models import Movies
from .serializers import MovieSerializer


class MovieList(APIView):

    authentication_classes = []
    permission_classes = []

    def get_obj(self, inst):
        try:
            obj = Movies.objects.filter(user=inst)
            return obj
        except ValueError:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def get(self, request, slug=None):
        instance = self.get_obj(slug)
        instance = MovieSerializer(instance, many=True)
        return Response(instance.data, status=status.HTTP_200_OK)


class AllMovies(APIView):

    authentication_classes = []
    permission_classes = []

    def get_obj(self):
        try:
            obj = Movies.objects.all()
            return obj
        except ValueError:
            return Response(status=status.HTTP_404_NOT_FOUND)
    
    def get(self, request):
        instance = self.get_obj()
        print(instance)
        instance = MovieSerializer(instance, many=True)
        return Response(instance.data, status=status.HTTP_200_OK)