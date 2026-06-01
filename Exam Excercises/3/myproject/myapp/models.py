from django.db import models
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.db.models import Sum

# Create your models here.

class Baker(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)
    email = models.EmailField()

    def __str__(self):
        return self.name

class Cake(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    weight = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField(null=True, blank=True)
    image = models.ImageField(upload_to="images/", null=True, blank=True)
    baker = models.ForeignKey(Baker, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.name

    def clean(self):
        if self.baker:

            count = Cake.objects.filter(baker=self.baker).exclude(pk=self.pk).count()
            if count >= 10:
                raise ValidationError("The baker already has 10 cakes")

            total_sum = Cake.objects.filter(baker=self.baker).exclude(pk=self.pk).aggregate(Sum('price'))['price__sum'] or 0
            if total_sum + self.price > 10000:
                raise ValidationError("The baker already has a sum of 10000")

            duplicate = Cake.objects.filter(name=self.name).exists()
            if duplicate:
                raise ValidationError("A cake with that name already exists")