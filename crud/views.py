from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib.auth import logout
from django.contrib.auth.models import User
from django.db import IntegrityError
# Create your views here.

def home(request):
    return render(request, 'home.html')

def signup(request):
    if request.method == 'GET':
        return render(request, 'signup.html',{'form' : UserCreationForm})
    else:
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.Objects.create_user(username=request.POST['username'], password=request.POST['password1'])
                user.save()
                login(request, user) # Genera la session
                return HttpResponse('Usuario creado exitosamente.')
            except IntegrityError:
                return render(request, 'signup.html',{'form' : UserCreationForm,
                                                      'error' : 'Username alredy exists'})
        return HttpResponse('Password dont match.')
    
def singout(request):
    logout(request)
    return redirect('home')