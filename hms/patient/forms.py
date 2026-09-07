from django import forms

from patient.models import Patient


class PatientForm(forms.ModelForm):
    class Meta:
        model = Patient
        fields='__all__'

    def clean_first_name(self):
        first_name = self.cleaned_data['first_name']
        if not first_name.isalpha():
            raise forms.ValidationError('First name must contain only letters')
        return first_name
    def clean_last_name(self):
        last_name = self.cleaned_data['last_name']
        if not last_name.isalpha():
            raise forms.ValidationError('Last name must contain only letters')
        return last_name

    def clean_phone(self):
        phone = self.cleaned_data['phone']
        if not phone.isdigit():
            raise forms.ValidationError('Phone number must contain numbers only')
        return phone
    def clean_blood_type(self):
        blood_type = self.cleaned_data['blood_type']
        blood_groups=['A+','A-','B+','B-','AB+','AB-','AB','O+','O-','O']
        if blood_type not in blood_groups:
            raise forms.ValidationError('Blood type must be one of ' + ",".join(blood_groups))
        return blood_type
