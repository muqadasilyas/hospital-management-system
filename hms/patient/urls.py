from . import views
from django.urls import path
urlpatterns = [
    path('', views.patient_list, name='patient'),
    path('<int:id>/',views.patient_detail, name='patient_detail'),
    path('create/',views.create_patient, name='patient_create'),
    path('<int:id>/edit/',views.update_patient, name='patient_update'),
    path('<int:id>/delete/',views.delete_patient, name='patient_delete'),
]