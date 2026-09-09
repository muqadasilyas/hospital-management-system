from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView,DeleteView,CreateView,UpdateView,DetailView
from doctor.forms import DoctorForm
from doctor.models import Doctor


# Create your views here.

class DoctorListView(LoginRequiredMixin,ListView):
    model = Doctor
    context_object_name = 'doctors'
    template_name = 'doctor/doctor_list.html'


class DoctorDetailView(LoginRequiredMixin,DetailView):
    model = Doctor
    template_name = 'doctor/doctor_detail.html'
    context_object_name = 'doctor'


class DoctorCreateView(LoginRequiredMixin,PermissionRequiredMixin,CreateView):
    model = Doctor
    form_class = DoctorForm
    template_name = 'doctor/doctor_form.html'
    success_url = reverse_lazy('doctor_list')
    permission_required = "doctor.add_doctor"

class DoctorUpdateView(LoginRequiredMixin,PermissionRequiredMixin,UpdateView):
    model = Doctor
    form_class = DoctorForm
    template_name = 'doctor/doctor_form.html'
    context_object_name = 'doctor'
    success_url = reverse_lazy('doctor_list')
    permission_required = "doctor.change_doctor"

class DoctorDeleteView(LoginRequiredMixin
,PermissionRequiredMixin,DeleteView):
    model = Doctor
    template_name = 'doctor/doctor_delete.html'
    context_object_name = 'doctor'
    success_url = reverse_lazy('doctor_list')
    permission_required = "doctor.delete_doctor"