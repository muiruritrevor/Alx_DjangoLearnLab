from django.contrib import admin
from django.urls import path
from .views import home, register, login_view, logout_view, profile


urlpatterns = [
    path('', home, name='home'),
    path('register/', register, name='register'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('profile/', profile, name='profile'),
]
