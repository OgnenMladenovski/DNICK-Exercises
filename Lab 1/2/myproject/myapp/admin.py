from django.contrib import admin
from .models import *

# Register your models here.

@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    list_display = ['type', 'name', 'date']

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'description', 'is_active']

@admin.register(Supplement)
class SupplementAdmin(admin.ModelAdmin):
    list_display = ['name', 'production_company', 'user', 'category']
    exclude = ['user']

    def save_model(self, request, obj, form, change):
        if not change or obj.user_id is None:
            obj.user = request.user
        return super().save_model(request, obj, form, change)
#tuka