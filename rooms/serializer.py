from rest_framework import serializers
from rooms.models import Room

class Room_serializer(serializers.ModelSerializer):
    class Meta:
        model = Room
        fields = ['room_id','type','sub_type','allocated_patient']


class Room_Create_serializer(serializers.Serializer):
    room_id = serializers.IntegerField()
    type = serializers.CharField()
    sub_type = serializers.CharField()

    def create(self,validated_data):
        return Room.objects.create(**validated_data)
