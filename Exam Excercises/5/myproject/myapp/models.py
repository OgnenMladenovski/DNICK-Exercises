from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Agent(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)
    linkedin = models.URLField()
    sales_done = models.PositiveIntegerField()
    email = models.EmailField()

    def __str__(self):
        return self.name

class PropertyFeatures(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)

class Property(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    area = models.FloatField()
    date = models.DateField()
    image = models.ImageField(upload_to='images/', null=True, blank=True)
    is_reserved = models.BooleanField(default=False)
    is_sold = models.BooleanField(default=False)
    agents = models.ManyToManyField(Agent, blank=True)
    features = models.ManyToManyField(PropertyFeatures, blank=True)

    def total_price(self):
        return sum(f.price for f in self.features.all())