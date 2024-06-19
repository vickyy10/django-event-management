from django.db import models

# Create your models here.


class Events(models.Model):
    eventname=models.CharField(max_length=100,unique=True)
    advanceprice=models.BigIntegerField()
    image=models.ImageField(upload_to='static/images',blank=True,null=True)
