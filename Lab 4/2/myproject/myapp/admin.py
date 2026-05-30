from django.contrib import admin
from .models import *

# Register your models here.
@admin.register(Trainer)
class TrainerAdmin(admin.ModelAdmin):
    def has_add_permission(self, request, obj=None):
        return True

@admin.register(Training)
class TrainingAdmin(admin.ModelAdmin):
    def has_add_permission(self, request, obj=None):
        return True