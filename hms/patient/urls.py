from . import views
from django.urls import path
urlpatterns = [
    path('patient/', views.patientList, name='patient'),
]