from django.db import models
from department.models import Department
# Create your models here.
class Doctor(models.Model):
    id=models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    specialization = models.CharField(max_length=50)
    phone = models.CharField(max_length=15)
    department=models.ForeignKey(Department,on_delete=models.CASCADE)

    def __str__(self):
        return self.name