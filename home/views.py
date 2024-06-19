from django.shortcuts import render,redirect
from django.contrib.auth import login,authenticate,logout
from django.contrib import messages
from .forms import ClientDetailsForm,ClientLoginform

# Create your views here.



def home(request):
    
    return render(request,'home.html')


def registration(request):
    if request.method == 'POST':
        form = ClientDetailsForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = ClientDetailsForm()
    return render(request, 'register.html', {'form': form})




def clientlogin(request):
    
    if request.method == 'POST':
        form = ClientLoginform(request.POST)    
    

        if form.is_valid():
            LoginUsername = form.cleaned_data.get('username')
            LoginPassword = form.cleaned_data.get('password')
            user = authenticate(request, username=LoginUsername, password=LoginPassword)

            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                messages.error(request, 'Invalid username or password.')
    else:
        form = ClientLoginform()

    return render(request,'Login.html', {'form': form})



def Clientlogout(request):

    logout(request)

    return redirect('home')