from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.db import models
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView,CreateView,DetailView,UpdateView,DeleteView

from appointments.forms import AppointmentForm
from appointments.models import Appointments
from doctor.models import Doctor


# Create your views here.

class AppointmentListView(LoginRequiredMixin,PermissionRequiredMixin,ListView):
    model=Appointments
    context_object_name='appointments'
    template_name = 'appointments/appointment_list.html'
    permission_required = "appointments.view_appointments"

    def get_queryset(self):
        user=self.request.user
        if user.is_superuser:
            return Appointments.objects.all()
        elif user.groups.filter(name='Doctors').exists():
            return Appointments.objects.filter(doctor=user.doctor).order_by('-appointment_date')
        elif user.groups.filter(name='Patient').exists():
            return Appointments.objects.filter(patient=user.patient).order_by('-appointment_date')
        elif user.groups.filter(name="Receptionist").exists():
            return Appointments.objects.all()
        return Appointments.objects.none()
class AppointmentCreateView(LoginRequiredMixin,PermissionRequiredMixin,CreateView):
    model=Appointments
    form_class = AppointmentForm
    template_name = 'appointments/appointment_form.html'
    success_url = reverse_lazy('appointment_list')
    permission_required = "appointments.add_appointments"

class AppointmentDetailView(LoginRequiredMixin,DetailView):
    model=Appointments
    context_object_name='appointment'
    template_name = 'appointments/appointment_detail.html'
    success_url = reverse_lazy('appointment_detail')
    def get_queryset(self):
        user=self.request.user
        if user.is_superuser:
            return Appointments.objects.all()
        elif user.groups.filter(name='Doctors').exists():
            return Appointments.objects.filter(doctor=user.doctor).order_by('-appointment_date')
        elif user.groups.filter(name='Patient').exists():
            return Appointments.objects.filter(patient=user.patient).order_by('-appointment_date')
        return Appointments.objects.none()

class AppointmentUpdateView(LoginRequiredMixin,PermissionRequiredMixin,UpdateView):
    model=Appointments
    context_object_name='appointment'
    form_class = AppointmentForm
    template_name = 'appointments/appointment_form.html'
    success_url = reverse_lazy('appointment_list')
    permission_required = "appointments.change_appointments"

class AppointmentDeleteView(LoginRequiredMixin,PermissionRequiredMixin,DeleteView):
    model=Appointments
    context_object_name='appointment'
    template_name = 'appointments/appointment_delete.html'
    success_url = reverse_lazy('appointment_list')
    permission_required = "appointments.delete_appointments"

class DoctorAppointmentListView(LoginRequiredMixin,ListView):
    model=Appointments
    context_object_name='appointments'
    template_name = 'appointments/appointment_list.html'
    def get_queryset(self):
        doctor_id=self.kwargs['doctor_id']
        return Appointments.objects.filter(doctor_id=doctor_id).order_by('-appointment_date')

class PatientAppointmentListView(LoginRequiredMixin,ListView):
    model=Appointments
    context_object_name='appointments'
    template_name = 'appointments/appointment_list.html'
    def get_queryset(self):
        patient_id=self.kwargs['patient_id']
        return Appointments.objects.filter(patient_id=patient_id).order_by('-appointment_date')

class AppointmentCompleteView(LoginRequiredMixin,PermissionRequiredMixin,UpdateView):
    model=Appointments
    permission_required = "appointments.complete_appointment"

    def get_queryset(self):
        user=self.request.user
        if user.is_superuser:
            return Appointments.objects.all()
        if user.groups.filter(name='Doctors').exists():
            return Appointments.objects.filter(doctor=user.doctor)
        return Appointments.objects.none()

    def form_valid(self, form):
        form.instance.status = "COMPLETED"
        return super().form_valid(form)