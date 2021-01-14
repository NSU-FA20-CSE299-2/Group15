from django.shortcuts import render
from django.http import HttpResponse
from .models import *
from django.forms import inlineformset_factory
from django.contrib.auth.forms import UserCreationForm


def home(request):
    return render(request, 'home.html')

def registerPage(request):
    form = UserCreationForm()
    context = {'form': form}
    return render(request, 'register.html', context)

def iptv(request):
    # getting all channels from database
    channels = Channel.objects.all()
    context = {'channels': channels}

    # rendering the site
    return render(request, 'iptv.html', context)
    
