from django.shortcuts import render
from django.http import HttpResponse
from .models import *


def home(request):
    return render(request, 'home.html')

def iptv(request):
    # getting all channels from database
    channels = Channel.objects.all()
    context = {'channels': channels}

    # rendering the site
    return render(request, 'iptv.html', context)
    
