from django.db import models
from datetime import date, datetime
from django.contrib.auth.models import User

# Create your models here.

class Doctor(models.Model):
    SPECIALTY = [
        ('cardiologist', 'cardiologist'),
        ('dermatologist', 'dermatologist'),
        ('neurologist', 'neurologist')
    ]
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=100)
    specialty = models.CharField(choices=SPECIALTY, max_length=100)
    image = models.ImageField(upload_to='images/', null=True, blank=True)
    institution = models.CharField(max_length=100)
    completed_appointments = models.PositiveIntegerField(default=0)
    email = models.EmailField()
    phone = models.CharField(max_length=100)

class Patient(models.Model):
    GENDER = [
        ("male", "MALE"),
        ("female", "FEMALE")
    ]
    full_name = models.CharField(max_length=100)
    birth_date = models.DateField()
    gender = models.CharField(choices=GENDER, max_length=100)
    email = models.EmailField()
    institution = models.CharField(max_length=100)

class Appointment(models.Model):
    TYPE = [
        ("cardiological", "cardiological"),
        ("dermatological", "dermatological"),
        ("neurological", "neurological"),
    ]

    STATUS = [
        ("scheduled", "scheduled"),
        ("in_progress", "in_progress"),
        ("completed", "completed")
    ]

    appointment_type = models.CharField(choices=TYPE, max_length=100)
    description = models.TextField()
    status = models.CharField(choices=STATUS, max_length=100, default='scheduled')
    datetime = models.DateTimeField()
    note = models.TextField(blank=True, null=True)
    responsible_doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)

class AppointmentAssignment(models.Model):
    appointment = models.ForeignKey(Appointment, on_delete=models.CASCADE)
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('appointment', 'doctor')