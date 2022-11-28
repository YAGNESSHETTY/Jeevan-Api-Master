from rest_framework import serializers
from patients.models import Patient

class Patient_serializer(serializers.ModelSerializer):
    class Meta:
        model = Patient
        fields = ['id','name','contact','allocated_room','allocated_doctor']


class Add_Patient(serializers.Serializer):
    name = serializers.CharField()
    contact = serializers.CharField()

    def create(self,validated_data):
        return Patient.objects.create(**validated_data)
