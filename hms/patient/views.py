from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.views.generic import ListView,DetailView,DeleteView,UpdateView,CreateView

from patient.forms import PatientForm
from patient.models import Patient
from django.shortcuts import get_object_or_404

# Create your views here.

class PatientListView(ListView):
    model = Patient
    context_object_name = 'patients'
    template_name = 'patient/patient_list.html'
class PatientDetailView(DetailView):
    model=Patient
    context_object_name='patient'
    template_name = 'patient/patient_detail.html'
class PatientCreateView(CreateView):
    model=Patient
    form_class=PatientForm
    template_name='patient/patient_form.html'
    success_url=reverse_lazy('patient')

class PatientUpdateView(UpdateView):
    model=Patient
    form_class=PatientForm
    template_name='patient/patient_form.html'
    success_url=reverse_lazy('patient')

class PatientDeleteView(DeleteView):
    model=Patient
    context_object_name='patient'
    template_name='patient/patient_delete.html'
    success_url=reverse_lazy('patient')