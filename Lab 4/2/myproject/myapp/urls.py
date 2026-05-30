from django.urls import path
from .views import *

app_name = "trainings"

urlpatterns = [
    path('index/', index, name='index'),
    path('trainings/add/', add_training, name='add_training')
]