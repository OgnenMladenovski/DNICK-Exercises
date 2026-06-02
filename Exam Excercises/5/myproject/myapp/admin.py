from django.contrib import admin
from .models import *
import datetime

# Register your models here.

# Кога еден оглас/недвижнина ќе се означи како продадена, потребно е сите агенти поврзани со неа да ја инкрементираат својата продажба

@admin.register(Agent)
class AgentAdmin(admin.ModelAdmin):
    list_display = ['name']

    def has_add_permission(self, request):
        if request.user.is_superuser:
            return True
        return False

@admin.register(PropertyFeatures)
class PropertyFeaturesAdmin(admin.ModelAdmin):
    list_display = ['name']

    def has_add_permission(self, request):
        if request.user.is_superuser:
            return True
        return False

@admin.register(Property)
class PropertyAdmin(admin.ModelAdmin):
    list_display = ['name', 'area', 'description']

    def has_add_permission(self, request):
        if hasattr(request.user, 'agent'):
            return True
        return False

    def save_model(self, request, obj, form, change):
        if not change or obj.user_id is None:
            obj.user = request.user
        return super().save_model(request, obj, form, change)

    def has_delete_permission(self, request, obj=None):
        if obj is None:
            return True
        return obj.features.count() == 0

    def has_view_permission(self, request, obj=None):
        return True

    def has_change_permission(self, request, obj=None):
        if obj is None:
            return True
        if hasattr(request.user, 'agent'):
            if request.user.agent in obj.agents.all():
                return True
        return False

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        if request.user.is_superuser:
            return qs.filter(date=datetime.date.today())
        return qs