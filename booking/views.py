from django.shortcuts import render,redirect

from .forms import bookingDetailsForm
from .models import bookingDetails
# Create your views here.



def EventBooking(request):
    if request.method == 'POST':
        form=bookingDetailsForm(request.POST)
        if form.is_valid():   
            data=form.save()
            print(data.id)
            return redirect('bookedDetails',data.id)           
    else:
        form=bookingDetailsForm()   
    return render(request,'eventBooking.html',{'form':form})




def bookedDetails(request,id=0):
    
    data = bookingDetails.objects.get(id=id)
    
    return render(request,'bookedDetails.html',{'data':data})