from django.contrib import admin
from .models import *
from django.db.models import Count

# Register your models here.

# Кога се брише турситичкиот водач, неговите дестинации по случаен избор се додаваат на остатите туристички водачи

@admin.register(TourGuide)
class TourGuideAdmin(admin.ModelAdmin):

    list_display = ["name", "surname", "phone", "email"]

    def has_change_permission(self, request, obj=None):
        if request.user.is_superuser:
            return True
        return False

    def has_delete_permission(self, request, obj=None):
        if request.user.is_superuser:
            return True
        return False

    def has_add_permission(self, request, obj=None):
        if request.user.is_superuser:
            return True
        return False

    def get_queryset(self, request):
        query_set = super().get_queryset(request)
        if request.user.is_superuser:
            return query_set.annotate(total_count=Count("tour")).filter(total_count__lt=3)
        return query_set
    # query - with a query we send a request to the database
    # queryset - the database returns what we request

@admin.register(Tour)
class TourAdmin(admin.ModelAdmin):

    list_display = ["destination", "price", "duration", "tour_guide"]

    def has_change_permission(self, request, obj=None):
        if obj is None:       # has to be first
            return True

        if request.user == obj.tour_guide.user:
            return True

        return False

    def has_view_permission(self, request, obj=None):
       return True