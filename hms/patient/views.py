from django.shortcuts import render
from django.http import HttpResponse

from patient.models import Patient
from django.shortcuts import get_object_or_404

# Create your views here.

def patient_list(request):
    patients = Patient.objects.all()
    return render(request,'patient/patient_list.html',{'patients':patients})

def patient_detail(request, id):
    patient=get_object_or_404(Patient,pk=id)
    return render(request,'patient/patient_detail.html',{'patient':patient})
