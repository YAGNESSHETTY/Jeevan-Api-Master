from django.shortcuts import render
from doctors.models import Doctor
from rest_framework.decorators import api_view
from doctors.serializers import Doctor_serializer,Add_Doctor_serializer
from django.http import JsonResponse
from rest_framework.parsers import JSONParser
# Create your views here.

@api_view(['GET'])
def list_doctors(request):
    doctor_list = Doctor.objects.all()
    serializer = Doctor_serializer(doctor_list,many=True)
    return JsonResponse(serializer.data,safe=False)

@api_view(['GET'])
def doctor_detail(request,pk):
    doctor_detail = Doctor.objects.get(pk=pk)
    serializer = Doctor_serializer(doctor_detail)
    return JsonResponse(serializer.data,safe=False)

@api_view(['POST'])
def add_doctor(request):
    data = JSONParser().parse(request)
    serialized_data = Add_Doctor_serializer(data=data)

    if serialized_data.is_valid():
        serialized_data.save()
        return JsonResponse(serialized_data.data,status=201)

    return JsonResponse(serialized_data.errors,status=400)