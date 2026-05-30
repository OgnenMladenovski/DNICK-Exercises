from django.urls import path
from .views import *

app_name = "movies"

urlpatterns = [
    path("index/", index, name="index"),
    path("movies/<int:pk>/", movie_details, name="movie_details")
]