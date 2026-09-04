from django.db import models

# Create your models here.
class Department(models.Model):
    id = models.AutoField(primary_key=True)
    department_name = models.TextField()
    department_description = models.TextField()

    def __str__(self):
        return self.department_name
