from django.urls import path
from . import views

urlpatterns = [
    path('', views.WatchListAV.as_view(), name='watch-list'),
    path('<str:pk>/', views.WatchListDetailAV.as_view(), name='watch-list-detail'),
    path('stream/', views.StreamPlatformAV.as_view(), name='stream'),
    path('stream/<str:pk>/', views.StreamPlatformDetailAV.as_view(), name='stream-detail'),
]