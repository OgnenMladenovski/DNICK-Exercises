from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('index/', views.index, name='index'),
    path('exhibitions/add/', views.add_exhibition, name='add_exhibition')
]
