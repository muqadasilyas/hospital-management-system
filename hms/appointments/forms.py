from django import forms

from appointments.models import Appointments


class AppointmentForm(forms.ModelForm):
    class Meta:
        model=Appointments
        fields="__all__"

