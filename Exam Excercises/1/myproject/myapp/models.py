from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Event(models.Model):
    name = models.CharField(max_length=100)
    date_time = models.DateTimeField()
    poster = models.ImageField(upload_to="images/", null=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    is_outside = models.BooleanField()

    def __str__(self):
        return self.name

class Band(models.Model):
    name = models.CharField(max_length=100, unique=True)
    country = models.CharField(max_length=100)
    date = models.DateField()
    number_of_appearences = models.PositiveIntegerField()

    def __str__(self):
        return self.name

class BandEvent(models.Model):
    band = models.ForeignKey(Band, on_delete=models.CASCADE)
    event = models.ForeignKey(Event, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.band} @ {self.event}"