from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.forms import inlineformset_factory
from django.contrib.auth.forms import UserCreationForm

from django.contrib import messages

from django.contrib.auth import authenticate, login, logout

from django.contrib.auth.decorators import login_required

from .models import *
from .forms import CreateUserForm


def home(request):
    return render(request, 'home.html')

def registerPage(request):
    if request.user.is_authenticated:
        return redirect('home')

    form = CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request, 'Account was created for ' + user)

            return redirect('login')

    context = {'form': form}
    return render(request, 'register.html', context)


def loginPage(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                messages.info(request, 'Username or Password is incorrect')

    context = {}
    return render(request, 'login.html', context)

def logoutUser(request):
    logout(request)
    return redirect('login')


@login_required(login_url='login')
def iptv(request):
    # getting all channels from database
    channels = Channel.objects.all()
    context = {'channels': channels}

    # rendering the site
    return render(request, 'iptv.html', context)
    
@login_required(login_url='login')
def vod(request):
    # getting all channels from database
    channels = Channel.objects.all()
    context = {'channels': channels}

    # rendering the site
    return render(request, 'vod.html', context)