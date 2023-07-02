from django.urls import path
from . import views

urlpatterns = [
    path('stream/', views.StreamList.as_view(), name='stream'),
    path('stream/<str:pk>/', views.StreamDetail.as_view(), name='stream-detail'),
    path('watchlist/', views.WatchListGV.as_view(), name='watch-list'),
    path('watchlist/<str:pk>/', views.WatchListDetailGV.as_view(), name='watch-list-detail'),
    path('watchlist/<str:pk>/reviews/', views.ReviewList.as_view(), name='reviews'),
    path('reviews/<str:pk>/', views.ReviewDetail.as_view(), name='review'),
]