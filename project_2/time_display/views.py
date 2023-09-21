from django.shortcuts import render
from time import strftime

def currentTime(request):
    time_dic = {
        "time": strftime("%Y-%m-%d %I:%M %p")
    }
    return render(request, 'index.html', time_dic)
