from . import views
from django.urls import path
urlpatterns = [
    path('', views.PatientListView.as_view(), name='patient'),
    path('<int:pk>/',views.PatientDetailView.as_view(), name='patient_detail'),
    path('create/',views.PatientCreateView.as_view(), name='patient_create'),
    path('<int:pk>/edit/',views.PatientUpdateView.as_view(), name='patient_update'),
    path('<int:pk>/delete/',views.PatientDeleteView.as_view(), name='patient_delete'),
]