from django.db import models
from doctor.models import Doctor
from patient.models import Patient
# Create your models here.
class Appointments(models.Model):
    id = models.AutoField(primary_key=True)
    appointment_date = models.DateField()
    appointment_time = models.TimeField()
    reason = models.TextField()
    status_choices={
        "P":"Pending",
        "R":"Rejected",
        "C":"Completed",
    }
    status = models.CharField(max_length=1,choices=status_choices)
    created_at = models.DateTimeField(auto_now_add=True)
    doctor = models.ForeignKey(Doctor,on_delete=models.CASCADE)
    patient = models.ForeignKey(Patient,on_delete=models.CASCADE)

    class Meta:
        permissions = [
            ("complete_appointment", "Can complete appointment"),
        ]
    def __str__(self):
        return self.reason