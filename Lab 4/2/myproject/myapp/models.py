from django.db import models

# Create your models here.
class Trainer(models.Model):
    name = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    experience = models.PositiveIntegerField()
    website = models.URLField()

    def __str__(self):
        return self.name

class Training(models.Model):
    class Category(models.TextChoices):
        CARDIO = 'Cardio'
        STRENGTH = 'Strength'
        YOGA = "Yoga"
        HIIT = "HIIT"
        PILATES = "Pilates"
        CROSS_FIT = "Cross-Fit"
        STRETCHING = "Stretching"

    class Level(models.TextChoices):
        BEGINNER = "Beginner"
        INTERMEDIATE = "Intermediate"
        ADVANCED = "Advanced"

    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='images/', null=True, blank=True)
    trainer = models.ForeignKey(Trainer, on_delete=models.CASCADE)
    category = models.CharField(choices=Category.choices)
    level = models.CharField(choices=Level.choices)
    duration = models.PositiveIntegerField()
    capacity = models.PositiveIntegerField()
    price = models.PositiveIntegerField()

    def __str__(self):
        return self.title