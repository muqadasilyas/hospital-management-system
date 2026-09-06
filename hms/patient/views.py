from django.shortcuts import render, redirect
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

def create_patient(request):
    if request.method=='POST':
        first_name=request.POST['first_name']
        last_name=request.POST['last_name']
        gender=request.POST['gender']
        age=request.POST['age']
        blood_type=request.POST['blood_type']
        phone=request.POST['phone']
        date_of_birth=request.POST['dob']
        patient=Patient.objects.create(first_name=first_name,
                                       last_name=last_name,
                                       gender=gender,
                                       dob=date_of_birth,
                                       phone=phone,
                                       blood_type=blood_type,
                                       age=age)
        return redirect('patient_detail',id=patient.id)
    return render(request,'patient/patient_form.html')