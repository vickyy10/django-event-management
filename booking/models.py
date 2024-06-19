from django.db import models

from admin.models import Events


# Create your models here.

class bookingDetails(models.Model):
    name=models.CharField(max_length=50)
    phonenumber=models.CharField(max_length=50)
    email=models.EmailField()
    date=models.DateField()
    event_type = models.ForeignKey(Events,on_delete=models.CASCADE)
    peoplestrength=models.BigIntegerField()

    
