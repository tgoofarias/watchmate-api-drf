from django.urls import path
from . import views

urlpatterns = [
    path('', views.MovieList.as_view(), name='movie-list'),
    path('<str:pk>/', views.MovieDetail.as_view(), name='movie-detail')
]