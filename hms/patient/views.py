from django.shortcuts import render, redirect
from django.http import HttpResponse

from patient.forms import PatientForm
from patient.models import Patient
from django.shortcuts import get_object_or_404

# Create your views here.

def patient_list(request):
    patients = Patient.objects.all()
    return render(request,'patient/patient_list.html',{'patients':patients})

def patient_detail(request, id):
    patient=get_object_or_404(Patient,pk=id)
    return render(request,'patient/patient_detail.html',{'patient':patient})

def create_patient(request):
    if request.method=='POST':
        form=PatientForm(request.POST)
        if form.is_valid():
            patient=form.save()
            return redirect('patient_detail', id=patient.id)
    else:
        form = PatientForm()

    return render(request,'patient/patient_form.html',
                  {'form':form})