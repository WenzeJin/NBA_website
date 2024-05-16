"""
views.py
Description: Views related to BBS
Author: Wenze Jin
Date: 2024/05/14
"""

from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.forms import UserCreationForm
from .forms import *
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages


# Create your views here.

def user_register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse('Registration successful')
        else:
            return HttpResponse('Form was invalid')
    else:
        form = UserCreationForm()
    return render(request, 'BBS/register.html', {'form': form})


def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, 'You are now logged in.')
            return redirect('BBS:index')
        else:
            messages.error(request, 'Invalid username or password')
            return redirect("BBS:login")
    else:
        form = UserLoginForm()
        return render(request, 'BBS/login.html', {'form': form})


def user_logout(request):
    logout(request)
    messages.success(request, 'You are now logged out!')
    return redirect("BBS:index")


def index(request):
    return render(request, 'BBS/index.html')
