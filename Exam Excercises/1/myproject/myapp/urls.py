from django.urls import path
from .views import *

urlpatterns = [
    path('index/', index, name='index'),
    path('events/add/', add_event, name='add_event')
]