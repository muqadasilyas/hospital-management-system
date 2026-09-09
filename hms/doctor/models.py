from django.db import models

import doctor
from department.models import Department
from django.contrib.auth.models import User
# Create your models here.
class Doctor(models.Model):
    id=models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    specialization = models.CharField(max_length=50)
    phone = models.CharField(max_length=15)
    department=models.ForeignKey(Department,on_delete=models.CASCADE)
    user=models.OneToOneField(User,on_delete=models.CASCADE,
                              null=True,blank=True, related_name='doctor')

    def __str__(self):
        return self.name