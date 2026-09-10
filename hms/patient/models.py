
from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone
# Create your models here.

class Patient(models.Model):
    id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    gender_choices = {
        'M': 'Male',
        'F': 'Female',
    }
    gender = models.CharField(max_length=1, choices=gender_choices)
    blood_type = models.CharField(max_length=2)
    dob = models.DateField()
    phone = models.CharField(max_length=15)
    user=models.OneToOneField(User,on_delete=models.CASCADE,blank=True,null=True)
    def __str__(self):
        return self.first_name + " " + self.last_name