from django.shortcuts import render, redirect
from . import models

def index(request):
    context = {
        "DOJOS": models.dojoRender
    }
    return render(request, 'index.html', context)
def dojo(request):
    models.dojoAdd(request)
    return redirect('/')
def ninja(request):
    models.ninjaAdd(request)
    return redirect('/')
def deleteDojo(request, dojo_id):
    models.removeDojo(request, dojo_id)
    return redirect('/')
