from django.contrib import admin
from .models import *

# Register your models here.

@admin.register(Band)
class BandAdmin(admin.ModelAdmin):
    list_display = ['name', "country"]

class BandEventInline(admin.TabularInline):
    model = BandEvent
    extra = 1

@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ['name', 'date_time']
    exclude = ['user']
    inlines = [BandEventInline]

    def save_model(self, request, obj, form, change):
        if not change or obj.user_id is None:
            obj.user = request.user
        return super().save_model(request, obj, form, change)

    def has_add_permission(self, request, obj=None):
        if request.user.is_superuser:
            return True
        return False


    def has_change_permission(self, request, obj=None):
        if obj and obj.user == request.user:
            return True
        return False

    def has_delete_permission(self, request, obj=None):
        if obj and obj.user == request.user and BandEvent.objects.filter(event=obj).count()==0:
            return True
        return False