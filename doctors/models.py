from django.db import models

# Create your models here.


class Doctor(models.Model):
    
    name = models.CharField(max_length=20)
    contact = models.CharField(max_length=10)

    def __str__(self):
        return self.name


