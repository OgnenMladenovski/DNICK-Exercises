from django.contrib import admin
from .models import *
from django.db.models import Q

# Register your models here.
@admin.register(Doctor)
class DoctorAdmin(admin.ModelAdmin):

    def has_add_permission(self, request, obj=None):
        if request.user.is_superuser:
            return True
        return False

@admin.register(Patient)
class PatientAdmin(admin.ModelAdmin):

    def has_add_permission(self, request, obj=None):
        if request.user.is_superuser:
            return True
        return False

@admin.register(Appointment)
class AppointmentAdmin(admin.ModelAdmin):

    def has_add_permission(self, request, obj=None):
        if hasattr(request.user, 'doctor') or request.user.is_superuser:
            return True
        return False

    def save_model(self, request, obj, form, change):
        if not change or obj.user_id is None:
            obj.user = request.user
            obj.responsible_doctor = Doctor.objects.get(user=request.user)
        return super().save_model(request, obj, form, change)

    def has_change_permission(self, request, obj=None):
        if request.user.is_superuser or request.user == obj.responsible_doctor.user:
            return True
        return False

    def has_delete_permission(self, request, obj=None):
        if obj.status == 'scheduled':
            return True
        return False

    def get_queryset(self, request):
        qs = super().get_queryset(request)

        if request.user.is_superuser:
            return qs

        doctor = Doctor.objects.get(user=request.user)

        return qs.filter(
            Q(responsible_doctor=doctor) |
            Q(appointmentassignment__doctor=doctor)
        ).distinct()
