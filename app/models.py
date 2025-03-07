from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from django.contrib.auth.models import AbstractUser
# from datetime import datetime
from django.utils import timezone

class CustomUser(AbstractUser):
    phone_number = PhoneNumberField(blank=True, region='IN')

    def __str__(self):
        return self.username

class Department(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name
    
class Note(models.Model):
    file_number = models.CharField(max_length=200)
    ref_no = models.CharField(max_length=100, blank=True, null=True)
    date = models.DateField(default=timezone.now)
    concerned_department = models.ForeignKey(Department, on_delete=models.CASCADE)
    subject = models.CharField(max_length=500, blank=True, null=True)
    comment = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.file_number
    
