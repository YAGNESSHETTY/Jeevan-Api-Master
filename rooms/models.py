from django.db import models

# from patients.models import room_id
# from patients.models import Patient,room_id

# Create your models here.

NORMAL='Normal_room'
ICU='Icu_room' 

AC='AC_room'
NON_AC='Non_AC_room'

   

type_choice=(
    (NORMAL,'Normal_room'),
    (ICU,'Icu_room')
)

room_choice=(
    (AC,'AC_room'),
    (NON_AC,'Non_AC_room')
)


class Room(models.Model):
    
    room_id = models.IntegerField(primary_key=True)
    type = models.CharField(max_length=11,choices=type_choice,default=NORMAL)
    sub_type = models.CharField(max_length=11,choices=room_choice,default=NON_AC)
    

    class Meta:
        ordering = ['room_id']

    def __str__(self):
        return str(self.room_id)


