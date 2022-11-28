from rest_framework import serializers
from doctors.models import Doctor

class Doctor_serializer(serializers.ModelSerializer):
    class Meta:
        model = Doctor
        fields = ['id','name','contact']

class Add_Doctor_serializer(serializers.Serializer):
    name = serializers.CharField()
    contact = serializers.CharField()

    def create(self,validated_data):
        return Doctor.objects.create(**validated_data)



