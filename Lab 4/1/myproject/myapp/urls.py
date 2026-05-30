from django.urls import path
from .views import *

app_name = "movies"

urlpatterns = [
    path("index/", index, name="index"),
    path("movies/<int:pk>/", movie_details, name="movie_details")
]

from django.urls import path
from .views import *

app_name = "books"

urlpatterns = [
    path('index/', index, name='index'),
    path('books/add/', add_book, name='add_book'),
    path('books/<int:pk>/', book_detail, name='book_detail'),
]
