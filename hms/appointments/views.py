from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView,CreateView,DetailView,UpdateView,DeleteView

from appointments.forms import AppointmentForm
from appointments.models import Appointments
from doctor.models import Doctor


# Create your views here.

class AppointmentListView(ListView):
    model=Appointments
    context_object_name='appointments'
    template_name = 'appointments/appointment_list.html'

    def queryset(self):
        return Appointments.objects.order_by('-appointment_date')

class AppointmentCreateView(CreateView):
    model=Appointments
    form_class = AppointmentForm
    template_name = 'appointments/appointment_form.html'
    success_url = reverse_lazy('appointment_list')

class AppointmentDetailView(DetailView):
    model=Appointments
    context_object_name='appointment'
    template_name = 'appointments/appointment_detail.html'
    success_url = reverse_lazy('appointment_list')

class AppointmentUpdateView(UpdateView):
    model=Appointments
    context_object_name='appointment'
    form_class = AppointmentForm
    template_name = 'appointments/appointment_form.html'
    success_url = reverse_lazy('appointment_list')

class AppointmentDeleteView(DeleteView):
    model=Appointments
    context_object_name='appointment'
    template_name = 'appointments/appointment_delete.html'
    success_url = reverse_lazy('appointment_list')

class DoctorAppointmentListView(ListView):
    model=Appointments
    context_object_name='appointments'
    template_name = 'appointments/appointment_list.html'

    def queryset(self):
        doctor_id=self.kwargs['doctor_id']
        return Appointments.objects.filter(doctor_id=doctor_id).order_by('-appointment_date')

class PatientAppointmentListView(ListView):
    model=Appointments
    context_object_name='appointments'
    template_name = 'appointments/appointment_list.html'
    def queryset(self):
        patient_id=self.kwargs['patient_id']
        return Appointments.objects.filter(patient_id=patient_id).order_by('-appointment_date')