from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.forms import inlineformset_factory
from django.contrib.auth.forms import UserCreationForm


from .models import *
from .forms import CreateUserForm


def home(request):
    return render(request, 'home.html')

def registerPage(request):
    form = CreateUserForm()
    
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')

    context = {'form': form}
    return render(request, 'register.html', context)


def loginPage(request):

    context = {}
    return render(request, 'login.html', context)

def iptv(request):
    # getting all channels from database
    channels = Channel.objects.all()
    context = {'channels': channels}

    # rendering the site
    return render(request, 'iptv.html', context)
    
