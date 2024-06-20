from django.shortcuts import render

from .forms import bookingDetailsForm

# Create your views here.

def EventBooking(request):
    
    form=bookingDetailsForm()

    
    return render(request,'eventBooking.html',{'form':form})