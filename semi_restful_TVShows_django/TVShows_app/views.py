from django.shortcuts import render, redirect
from . import models

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
    models.update_model(request, showID)
    return redirect(f'/shows/{models.Show.objects.get(id = showID).id}')