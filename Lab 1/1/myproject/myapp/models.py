from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Instructor(models.Model):
    class Experience(models.TextChoices):
        BEGINNER = "Beginner"
        CERTIFIED = "Certified"
        PROFESSIONAL = "Professional"

    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    biography = models.TextField(null=True, blank=True)
    experience = models.CharField(choices=Experience.choices)

    def __str__(self):
        return self.name

class Category(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)
    availability = models.BooleanField(default=False)

    def __str__(self):
        return self.name

class Training(models.Model):
    name = models.CharField(max_length=100)
    instructor = models.ForeignKey(Instructor, on_delete=models.CASCADE)
    description = models.TextField(null=True, blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to="images/", null=True, blank=True)
    price = models.PositiveIntegerField()
    available_spots = models.PositiveIntegerField()

    def __str__(self):
        return self.name


