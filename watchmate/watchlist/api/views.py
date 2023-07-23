from rest_framework.permissions import IsAuthenticated
from rest_framework import generics
from rest_framework.exceptions import ValidationError

from watchlist.models import WatchList, StreamPlatform, Review
from .serializers import WatchListSerializer, StreamPlatformSerializer, ReviewSerializer
from .permissions import AdminOrReadOnly, ReviewUserOrReadOnly


class ReviewList(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = ReviewSerializer

    def get_queryset(self):
        pk = self.kwargs['pk']
        return Review.objects.filter(watchlist=pk)

    def perform_create(self, serializer):
        user = self.request.user

        watchlist_id = self.kwargs.get('pk')
        watchlist = WatchList.objects.get(id=watchlist_id)

        if not user.is_authenticated:
            raise ValidationError('Please login to make a review.')
        try:
            Review.objects.get(user=user)
            raise ValidationError('User already have a review.')
        except Review.DoesNotExist:
            pass

        if watchlist.number_rating == 0:
            print(watchlist.number_rating)
            watchlist.rating = serializer.validated_data['rating']
        else:
            watchlist.rating = (watchlist.rating + serializer.validated_data['rating'])/2
        watchlist.number_rating += 1
        watchlist.save()
        
        serializer.save(watchlist=watchlist, user=user)


class ReviewDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    permission_classes = [ReviewUserOrReadOnly]


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
