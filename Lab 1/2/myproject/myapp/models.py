from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Company(models.Model):
    TYPE = [
        {"SM", "SMALL"},
        {"MD", "MEDIUM"},
        {"LG", "LARGE"}
    ]

    type = models.CharField(choices=TYPE)
    name = models.CharField(max_length=100)
    date = models.DateField()

    def __str__(self):
        return self.name

class Category(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)
    is_active = models.BooleanField()

    def __str__(self):
        return self.name

class Supplement(models.Model):
    name = models.CharField(max_length=100)
    production_company = models.ForeignKey(Company, on_delete=models.CASCADE)
    description = models.TextField(null=True, blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name