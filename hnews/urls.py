from django.contrib import admin
from django.urls import path, include
from .views import PostsList

urlpatterns = [
    path('posts/', PostsList.as_view()),
]