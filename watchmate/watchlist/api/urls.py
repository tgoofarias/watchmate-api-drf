from django.urls import path
from . import views

urlpatterns = [
    path('', views.movie_list, name='movie-list'),
    path('<str:pk>/', views.movie_detail, name='movie-detail')
]