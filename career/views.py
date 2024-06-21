from django.shortcuts import render

from .forms import careermodelform


# Create your views here.


def jobapply(request):
   
    if request.method == 'POST':
       
        form=careermodelform(request.POST,request.FILES)

        if form.is_valid():
           
            form.save()

    else:
        form=careermodelform()

    return render(request,'career.html',{'form':form})