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
from .models import *


# Create your views here.

def user_register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            create_user_info(user)
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
            create_user_info_condition(user)
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
    logged_in = request.user.is_authenticated
    user_info = None
    if logged_in:
        logged_in = True
        create_user_info_condition(request.user)
        user_info = UserInfo.objects.filter(user=request.user)
        user_info = user_info[0]
    else:
        logged_in = False
    return render(request, 'BBS/index.html', {'nickname': user_info.nickname if logged_in else ""})


def user_profile(request):
    logged_in = request.user.is_authenticated
    user_info = None
    if logged_in:
        logged_in = True
        create_user_info_condition(request.user)
        user_info = UserInfo.objects.filter(user=request.user)
        user_info = user_info[0]
    else:
        logged_in = False
    return render(request, 'BBS/profile.html', {'logged_in': logged_in, 'user_info': user_info})


def edit_profile(request):
    logged_in = request.user.is_authenticated
    user_info = None
    form = None
    if logged_in:
        logged_in = True
        create_user_info_condition(request.user)
        user_info = UserInfo.objects.filter(user=request.user)
        user_info = user_info[0]
        form = UserInfoForm(instance=user_info)
    else:
        logged_in = False
        form = UserInfoForm()
    if request.method == 'POST':
        form = UserInfoForm(request.POST, instance=user_info)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profile saved successfully.')
            return redirect('BBS:profile')
        else:
            messages.error(request, 'Form was invalid')
            return redirect('BBS:profile-edit')
    else:
        return render(request, 'BBS/profile_edit.html', {'logged_in': logged_in, 'user_info': user_info, 'form': form})
