
from django.urls import path
from . import views

urlpatterns = [
    path('booking',views.EventBooking,name='eventbooking'),  
]