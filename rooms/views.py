from django.shortcuts import render
from rooms.models import Room
from rest_framework.decorators import api_view
from rooms.serializer import Room_serializer,Room_Create_serializer
from django.http import JsonResponse
from rest_framework.parsers import JSONParser
# Create your views here.

@api_view(['GET'])
def list_rooms(request):
    room_list = Room.objects.all()
    serializer = Room_serializer(room_list,many=True)
    return JsonResponse(serializer.data,safe=False)

@api_view(['GET'])
def room_detail(request,pk):
    patient_detail = Room.objects.get(pk=pk)
    serializer = Room_serializer(patient_detail)
    return JsonResponse(serializer.data,safe=False)

@api_view(['POST'])
def add_room(request):
    data = JSONParser().parse(request)
    serialized_data = Room_Create_serializer(data=data)
    if serialized_data.is_valid():
        serialized_data.save()
        return JsonResponse(serialized_data.data,status=201)

    return JsonResponse(serialized_data.errors, status=400)

