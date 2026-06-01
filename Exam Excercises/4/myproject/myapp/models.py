from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Artist(models.Model):
    class Style(models.TextChoices):
        IMPRESSIONISM = "Impressionism"
        POP_ART = "Pop Art"
        GRAFFITI = "Graffiti"

    name = models.CharField(max_length=100)
    style = models.CharField(choices=Style.choices)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Exhibition(models.Model):
    title = models.CharField(max_length=100)
    date_start = models.DateField()
    date_end = models.DateField()
    description = models.TextField()
    location = models.CharField(max_length=100)

    def __str__(self):
        return self.title

class Art(models.Model):
    title = models.CharField(max_length=100)
    date = models.DateField()
    image = models.ImageField(upload_to='images/', null=True, blank=True)

    exhibition = models.ForeignKey(Exhibition, on_delete=models.CASCADE)
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
