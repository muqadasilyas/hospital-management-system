from django.urls import path

from appointments.views import AppointmentListView, AppointmentDetailView, AppointmentUpdateView, AppointmentDeleteView, \
    AppointmentCreateView, DoctorAppointmentListView, PatientAppointmentListView

urlpatterns = [
    path('',AppointmentListView.as_view(),name='appointment_list'),
    path('<int:pk>/',AppointmentDetailView.as_view(),name='appointment_detail'),
    path('<int:pk>/update/',AppointmentUpdateView.as_view(),name='appointment_update'),
    path('<int:pk>/delete/',AppointmentDeleteView.as_view(),name='appointment_delete'),
    path('create/',AppointmentCreateView.as_view(),name='appointment_create'),
    path('<int:doctor_id>/doctor/',DoctorAppointmentListView.as_view(),name='doctor_appointment_list'),
    path('<int:patient_id>/patient/',PatientAppointmentListView.as_view(),name='patient_appointment_list'),

]