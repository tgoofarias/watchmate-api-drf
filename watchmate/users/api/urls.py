from django.urls import path

from rest_framework.authtoken.views import obtain_auth_token

from users.api import views

urlpatterns = [
    path('login/', obtain_auth_token, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('account/', views.account_view, name='account'),
    path('register/', views.registration_view, name='register'),
]