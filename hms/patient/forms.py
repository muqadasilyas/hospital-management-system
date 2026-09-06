from django import forms

from patient.models import Patient


class PatientForm(forms.ModelForm):
    class Meta:
        model = Patient
        fields='__all__'