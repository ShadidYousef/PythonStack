from django.shortcuts import render, redirect
from . import models
from django.contrib import messages

def root(request):
    return redirect('/shows')

def shows(request):
    context = {
        "SHOWS": models.getShows_model(request)
    }
    return render(request, 'shows.html', context)

def renderAddShow(request):
    return render(request, 'addShow.html')

def addShow(request):
    errors = models.Show.objects.basic_validator(request.POST)
    if len(errors) > 0:
        for k, v in errors.items():
            messages.error(request, v)
        return redirect('/shows/new')
    else:
        models.addShow_model(request)
        return redirect(f'/shows/{models.Show.objects.last().id}')

def showInfo(request, showID):
    context = {
        "SHOW_INFO": models.getShowInfo_model(request, showID)
    }
    return render(request, 'showInfo.html', context)

def delete(request, showID):
    models.delete_model(request, showID)
    return redirect('/shows')

def renderEditShow(request, showID):
    context = {
        "SHOW_INFO": models.getShowInfo_model(request, showID)
    }
    return render(request, 'editShow.html', context, showID)

def update(request, showID):
    errors = models.Show.objects.basic_validator(request.POST)
    if len(errors) > 0:
        for k, v in errors.items():
            messages.error(request, v)
        return redirect(f'/shows/{models.Show.objects.get(id = showID).id}/edit')
    else:
        models.update_model(request, showID)
        return redirect(f'/shows/{models.Show.objects.get(id = showID).id}')