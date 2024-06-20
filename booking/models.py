from django.db import models

from event_admin.models import Events




# Create your models here.

class bookingDetails(models.Model):
    name=models.CharField(max_length=50)
    phonenumber=models.CharField(max_length=50)
    email=models.EmailField()
    date=models.DateField()
    Adress_line_1=models.CharField(max_length=100)
    Adress_line_2=models.CharField(max_length=100)
    state=models.CharField(max_length=100)
    pin=models.IntegerField()
    event_type = models.ForeignKey(Events,on_delete=models.CASCADE)
    peoplestrength=models.BigIntegerField()

    
