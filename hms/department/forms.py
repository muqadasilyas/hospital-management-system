from django import forms

from department.models import Department


class DepartmentForm(forms.ModelForm):
    class Meta:
        model = Department
        fields = "__all__"

    def clean_department_name(self):
        department_name = self.cleaned_data['department_name']
        if not department_name.isalpha():
            raise forms.ValidationError("Department name must be alphanumeric")
        return department_name
