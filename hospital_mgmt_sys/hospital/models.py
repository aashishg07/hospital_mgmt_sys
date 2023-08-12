from django.db import models

# Create your models here.

gender_choices = (
    ("Male", "Male"),
    ("Female", "Female"),
    ("Others", "Others")
)

class Doctor(models.Model):
    name = models.CharField(max_length=255)
    phone = models.IntegerField()
    special = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Patient(models.Model):
    name = models.CharField(max_length=255)
    phone = models.IntegerField()
    gender = models.CharField(max_length=20, choices=gender_choices, default="Male")
    age = models.IntegerField()
    problem = models.TextField()

    def __str__(self):
        return self.name


class Appointment(models.Model):
    doctor_app = models.ForeignKey(Doctor, related_name="doctor", on_delete=models.CASCADE)
    patient_app = models.ForeignKey(Patient, related_name="patient", on_delete=models.CASCADE)
    date = models.DateField(auto_now=True)
    time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.doctor.name + " " + self.patient.name

