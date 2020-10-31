"""paths and viws for users authentication"""
from django.urls import path
from django.contrib.auth import views
from .import views as create_views

app_name = 'users'

urlpatterns = [
    path('login/', views.LoginView.as_view(), name='login'),
    path('register/', create_views.register, name='register'),
    path('logout/', views.LogoutView.as_view(), name='logout')
]
