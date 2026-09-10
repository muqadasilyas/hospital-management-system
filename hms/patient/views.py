from typing import Any

from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpRequest
from django.urls import reverse_lazy
from django.views.generic import ListView,DetailView,DeleteView,UpdateView,CreateView
from datetime import date

import patient
from patient.forms import PatientForm
from patient.models import Patient
from django.shortcuts import get_object_or_404

# Create your views here.

class PatientListView(LoginRequiredMixin,ListView):
    model = Patient
    context_object_name = 'patients'
    template_name = 'patient/patient_list.html'

    def get(self, request: HttpRequest, *args: Any, **kwargs: Any):
        print("User: ",request.user)
        print("Authenticated: ",request.user.is_authenticated)
        return super().get(request, *args, **kwargs)
    def get_queryset(self):
        user=self.request.user
        if user.is_superuser:
            patients = Patient.objects.all()
        elif user.groups.filter(name='Doctors').exists():
            patients = Patient.objects.filter(appointments__doctor=user.doctor).distinct()

        elif user.groups.filter(name='Patient').exists():
            patients = Patient.objects.filter(id=user.patient.id)

        else:
            patients = Patient.objects.none()



        today = date.today()

        for patient in patients:
            age = today.year - patient.dob.year

            if (today.month, today.day) < (
                    patient.dob.month,
                    patient.dob.day
            ):
                age -= 1

            patient.age = age

        return patients


class PatientDetailView(LoginRequiredMixin,DetailView):
    model=Patient
    context_object_name='patient'
    template_name = 'patient/patient_detail.html'
    def get_context_data(self, **kwargs):
        context=super().get_context_data(**kwargs)
        today=date.today()
        patient=self.object
        age=today.year-patient.dob.year
        if (today.month,today.day) < (patient.dob.month,patient.dob.day):
            age-=1
        context['age']=age
        return context
class PatientCreateView(LoginRequiredMixin,PermissionRequiredMixin,CreateView):
    model=Patient
    form_class=PatientForm
    template_name='patient/patient_form.html'
    success_url=reverse_lazy('patient')
    permission_required = "patient.add_patient"

class PatientUpdateView(LoginRequiredMixin,PermissionRequiredMixin,UpdateView):
    model=Patient
    form_class=PatientForm
    template_name='patient/patient_form.html'
    success_url=reverse_lazy('patient')
    permission_required = "patient.change_patient"

class PatientDeleteView(LoginRequiredMixin,PermissionRequiredMixin,DeleteView):
    model=Patient
    context_object_name='patient'
    template_name='patient/patient_delete.html'
    success_url=reverse_lazy('patient')
    permission_required = "patient.delete_patient"