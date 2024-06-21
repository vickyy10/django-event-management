from django.db import models

# Create your models here.



class Events(models.Model):
    eventname=models.CharField(max_length=100,unique=True)
    advanceprice=models.BigIntegerField()
    image=models.ImageField(upload_to='eventIMGS',blank=True,null=True)

    def __str__(self):
        
        return self.eventname
    
class CareerAvailability(models.Model):
    position=models.CharField( max_length=50)

    def __str__(self):

        return self.position

