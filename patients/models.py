from django.db import models
from doctors.models import Doctor
from rooms.models import Room


# Create your models here.

        

class Patient(models.Model):
    name = models.CharField(max_length=20)
    contact = models.CharField(max_length=10)
    allocated_room = models.OneToOneField(Room,on_delete=models.CASCADE,related_name='allocated_patient',default=None,null=True,blank=True)
    allocated_doctor = models.ForeignKey(Doctor,on_delete=models.CASCADE,related_name='patients',default=None,null=True,blank=True)

    def __str__(self):
        return self.name


