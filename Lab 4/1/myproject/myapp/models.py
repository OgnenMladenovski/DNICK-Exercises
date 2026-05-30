from django.db import models

# Create your models here.
class ProductionHouse(models.Model):
    name = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    founding_year = models.DateField()
    link = models.URLField()

    def __str__(self):
        return self.name

class Movie(models.Model):
    class Genre(models.TextChoices):
        ACTION = "Action"
        COMEDY = "Comedy"
        DRAMA = "Drama"
        HORROR = "Horror"
        SCI_FI = "Sci-Fi"
        DOCUMENTARY = "Documentary"
        ANIMATED = "Animated"

    class Type(models.TextChoices):
        DIGITAL = "Digital"
        BLU_RAY = "Blu-Ray"
        DVD = "DVD"

    title = models.CharField(max_length=100)
    poster = models.ImageField(upload_to="movies/", null=True, blank=True)
    IMDB = models.CharField(max_length=100)
    release_year = models.DateField()
    production_house = models.ForeignKey(ProductionHouse, on_delete=models.CASCADE, related_name="movies")
    duration_minutes = models.PositiveIntegerField()
    genre = models.CharField(choices = Genre.choices)
    type = models.CharField(choices = Type.choices)
    price = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        return self.title