from django.contrib import admin
from .models import *

# Register your models here.

@admin.register(Instructor)
class InstructorAdmin(admin.ModelAdmin):
    list_display = ['name', 'surname', 'experience']

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'description', 'availability']

@admin.register(Training)
class TrainingAdmin(admin.ModelAdmin):
    list_display = ['name', 'instructor', 'user', 'category', 'price', 'available_spots']
    exclude = ['user']

    def save_model(self, request, obj, form, change):
        obj.user = request.user
        return super().save_model(request, obj, form, change)
