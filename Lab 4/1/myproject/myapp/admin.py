from django.contrib import admin
from .models import *

# Register your models here.
@admin.register(ProductionHouse)
class ProductionHouseAdmin(admin.ModelAdmin):
    ...

@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    ...
