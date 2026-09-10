from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.db.models import QuerySet
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
    def get_queryset(self):
        user=self.request.user
        if user.is_superuser:
            return Doctor.objects.all()
        elif user.groups.filter(name="Doctors").exists():
            return Doctor.objects.filter(id=user.doctor.id)
        elif user.groups.filter(name="Patient").exists():
            return Doctor.objects.filter(appointments__patient=user.patient.id)
        else:
            return Doctor.objects.none()

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