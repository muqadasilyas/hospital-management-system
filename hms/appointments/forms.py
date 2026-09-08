from django import forms

from appointments.models import Appointments


class AppointmentForm(forms.ModelForm):
    class Meta:
        model=Appointments
        fields=["reason","status","doctor","patient"]
        read_only_fields=("appointment_date","appointment_time","created_at")
