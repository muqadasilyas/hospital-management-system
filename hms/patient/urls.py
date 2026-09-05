from . import views
from django.urls import path
urlpatterns = [
    path('', views.patient_list, name='patient'),
    path('<int:id>/',views.patient_detail, name='patient_detail')
]