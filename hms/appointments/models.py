from django.db import models
from doctor.models import Doctor
from patient.models import Patient
# Create your models here.
class Appointments(models.Model):
    id = models.AutoField(primary_key=True)
    appointment_date = models.DateField(auto_now_add=True)
    appointment_time = models.TimeField(auto_now_add=True)
    reason = models.TextField()
    status = models.BooleanField()
    created_at = models.DateTimeField(auto_now_add=True)
    doctor = models.ForeignKey(Doctor,on_delete=models.CASCADE)
    patient = models.ForeignKey(Patient,on_delete=models.CASCADE)

    class Meta:
        permissions = [
            ("complete_appointment", "Can complete appointment"),
        ]
    def __str__(self):
        return self.reason