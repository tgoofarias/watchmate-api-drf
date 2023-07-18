from rest_framework import generics
from rest_framework.exceptions import ValidationError

from watchlist.models import WatchList, StreamPlatform, Review
from .serializers import WatchListSerializer, StreamPlatformSerializer, ReviewSerializer


class ReviewList(generics.ListCreateAPIView):
    serializer_class = ReviewSerializer

    def get_queryset(self):
        pk = self.kwargs['pk']
        return Review.objects.filter(watchlist=pk)

    def perform_create(self, serializer):
        user = self.request.user

        if not user.is_authenticated:
            raise ValidationError('Please login to make a review.')
        elif Review.objects.get(user=user):
            raise ValidationError('User already have a review.')

        watchlist_id = self.kwargs.get('pk')
        watchlist = WatchList.objects.get(id=watchlist_id)
        serializer.save(watchlist=watchlist, user=user)


class ReviewDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer


class WatchListGV(generics.ListCreateAPIView):
    queryset = WatchList.objects.all()
    serializer_class = WatchListSerializer


class WatchListDetailGV(generics.RetrieveUpdateDestroyAPIView):
    queryset = WatchList.objects.all()
    serializer_class = WatchListSerializer
    lookup_field = 'pk'


class StreamList(generics.ListCreateAPIView):
    queryset = StreamPlatform.objects.all()
    serializer_class = StreamPlatformSerializer


class StreamDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = StreamPlatform.objects.all()
    serializer_class = StreamPlatformSerializer
    lookup_field = 'pk'
