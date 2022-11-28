from django.shortcuts import render
from patients.models import Patient
from rest_framework.decorators import api_view
from patients.serializer import Patient_serializer,Add_Patient
from django.http import JsonResponse
from rest_framework.parsers import JSONParser
# Create your views here.

@api_view(['GET'])
def list_patients(request):
    patient_list = Patient.objects.all()
    serializer = Patient_serializer(patient_list,many=True)
    return JsonResponse(serializer.data,safe=False)

@api_view(['GET'])
def patient_detail(request,pk):
    patient_detail = Patient.objects.get(pk=pk)
    serializer = Patient_serializer(patient_detail)
    return JsonResponse(serializer.data,safe=False)

@api_view(['POST'])
def add_patient(request):
    data = JSONParser().parse(request)
    serialized_data = Add_Patient(data=data)
    if serialized_data.is_valid():
        serialized_data.save()
        return JsonResponse(serialized_data.data,status=201)

    return JsonResponse(serialized_data.errors,status=400)


    