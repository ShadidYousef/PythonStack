from django.shortcuts import render, redirect
from . import models
from django.contrib import messages
import bcrypt

def index(request):
    return render(request, 'index.html')

def register(request):
    errors = models.User.objects.basic_validator(request.POST)
    if len(errors) > 0:
        for k, v in errors.items():
            messages.error(request, v)
        return redirect('/')
    else:
        return models.register_model(request)

def login(request):
    return models.login_model(request)


def success(request):
    context = {
        "user": models.user_session_model(request)
    }
    return render(request, 'success.html', context)


def logout(request):
    del request.session['userid']
    return redirect('/')