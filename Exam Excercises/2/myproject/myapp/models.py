from django.db import models
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.db.models import Sum

# Create your models here.

class TourGuide(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE) # reminder
    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    phone = models.PositiveIntegerField()
    email = models.EmailField()

    def __str__(self):
        return self.name

class Tour(models.Model):
    destination = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    duration = models.PositiveIntegerField()
    image = models.ImageField(upload_to='images/', null=True, blank=True)
    tour_guide = models.ForeignKey(TourGuide, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return f"{self.destination} - {self.tour_guide}"

    def clean(self):        # cleaning of the database (filtering)
        if self.tour_guide:

            count = Tour.objects.filter(tour_guide = self.tour_guide).count()
            if count >= 5:
                raise ValidationError("Водачот веќе има 5 дестинации")

            price_count = Tour.objects.filter(tour_guide = self.tour_guide).aggregate(Sum('price'))['price__sum'] or 0
            if price_count + self.price > 50000:
                raise ValidationError("Водачот веќе има над 50000 цена")

            duplicate = Tour.objects.filter(destination = self.destination).exists()
            if duplicate:
                raise ValidationError("Постои дестинацијата")