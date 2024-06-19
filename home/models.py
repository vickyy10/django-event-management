from django.db import models

# Create your models here.


from django.contrib.auth.models import AbstractUser

class ClientDetails(AbstractUser):
    
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    address = models.CharField(max_length=255, blank=True, null=True)

    USERNAME_FIELD = 'username'
    
    def __str__(self):
        return self.username


