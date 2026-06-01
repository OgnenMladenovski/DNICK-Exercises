from django.contrib import admin
from .models import *
import datetime

# Register your models here.

@admin.register(Artist)
class ArtistAdmin(admin.ModelAdmin):
    list_display = ['name', 'style']

    def has_add_permission(self, request, obj=None):
        return request.user.is_superuser

@admin.register(Exhibition)
class ExhibitionAdmin(admin.ModelAdmin):
    list_display = ['title', 'date_start', 'date_end', 'location']

    def has_add_permission(self, request, obj=None):
        return request.user.is_superuser

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        today = datetime.date.today()

        if request.user.is_superuser:
            return qs.filter(end_date__gt=today)

        if hasattr(request.user, 'artist'):
            artist = request.user.artist
            return qs.filter(artwork__artist=artist).distinct()

        return qs

@admin.register(Art)
class ArtAdmin(admin.ModelAdmin):
    list_display = ['title', 'date']

    def save_model(self, request, obj, form, change):
        if not change and hasattr(request.user, 'artist'):
            obj.user = request.user.artist
        return super().save_model(request, obj, form, change)

    def has_change_permission(self, request, obj=None):
        if obj is None:
            return True
        if request.user.is_superuser:
            return True
        if obj.user and obj.user.user == request.user:
            return True
        return False