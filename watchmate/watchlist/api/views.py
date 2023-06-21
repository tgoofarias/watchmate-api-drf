from rest_framework.response import Response
from rest_framework.decorators import api_view

from watchlist.models import Movie
from .serializers import MovieSerializer

@api_view(['GET'])
def movie_list(request):
    movies = Movie.objects.all()
    serializer = MovieSerializer(instance=movies, many=True)
    return Response(data=serializer.data)

@api_view(['GET'])
def movie_detail(request, pk):
    movie = Movie.objects.get(id=pk)
    serializer = MovieSerializer(instance=movie, many=False)
    return Response(data=serializer.data)