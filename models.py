
from django.db import models
from datetime import timezone
from django.utils.timezone import now


# Create your models here.

class Doctor(models.Model):
    doctor_name = models.CharField(max_length=50)
    photo = models.FileField(blank=True)
    specialization = models.CharField(max_length=20)
    available = models.BooleanField(default=True)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.doctor_name

class Patient(models.Model):
    patient_name = models.CharField(max_length=50)
    age = models.IntegerField(default=0)
    sex = models.CharField(max_length=10)
    pub_date = models.DateTimeField('date published')
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)

    def __str__(self):
        return self.patient_name


class Prescription(models.Model):
    doctor = models.ForeignKey(Doctor,on_delete=models.CASCADE)
    disease = models.CharField(max_length=50)
    patient = models.ForeignKey(Patient,on_delete=models.CASCADE)
    title = models.CharField(max_length=30)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return "%s %s" %(self.title, self.disease)

class UserCustom(models.Model):
    firstname = models.CharField(max_length=50)
    lastname = models.CharField(max_length=30)
    email = models.EmailField(max_length=50)
    username = models.CharField(max_length=30)
    password = models.CharField(max_length=30)

    def __str__(self):
        return self.username


class session(models.Model):
    username = models.CharField(max_length=30)
    key = models.UUIDField(max_length=30)

    def __str__(self):
        return self.username





