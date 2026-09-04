from . import views
from django.urls import path
urlpatterns = [
    path('patient/', views.patient_list, name='patient'),
]