from django.contrib.auth import login, authenticate, logout
from django.shortcuts import render, redirect
from django.conf import settings
from . import forms
import authentication.forms


def login_page(request):
    form = authentication.forms.LoginForm()
    message = ''
    if request.method == 'POST':
        form = authentication.forms.LoginForm(request.POST)
        if form.is_valid():
            user = authenticate(
                username=form.cleaned_data['username'],
                password=form.cleaned_data['password'],
            )
            if user is not None:
                login(request, user)
                #message = f'Bonjour, {user.username}! Vous êtes connecté.'
                return redirect('home')
        message = 'Identifiants invalides.'
    return render(
        request, 'authentication/login.html', context={'form': form, 'message': message})


def signup_page(request):
    form = forms.SignupForm()
    if request.method == 'POST':
        form = forms.SignupForm(request.POST)
        if form.is_valid():
            user = form.save()
            # auto-login user
            login(request, user)
            return redirect(settings.LOGIN_REDIRECT_URL)
    return render(request, 'authentication/signup.html', context={'form': form})