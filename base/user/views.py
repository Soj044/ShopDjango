from django.contrib import auth
from django.contrib.auth import logout
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.urls import reverse

from .forms import UserLoginForm, UserRegistrationForm
from .models import *


def user_register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)  # ПОПРОБОВАТЬ УБРАТЬ ЭТО(ЧТО БУДЕТ???)
            user.set_password(form.cleaned_data['password1'])
            user.save()
            return render(request, 'user/register_done.html')
    else:
        form = UserRegistrationForm()
    return render(request, 'user/register.html', {'form': form})


def user_profile(request):
    return render(request, 'user/profile.html')


def user_login(request):
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = auth.authenticate(username=username, password=password)

            if user:
                auth.login(request, user)
                return HttpResponseRedirect(reverse('shop:cat_index'))
    else:
        form = UserLoginForm()
    return render(request, 'user/login.html', {'form': form})


def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('user:login'))

