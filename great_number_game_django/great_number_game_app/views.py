from django.shortcuts import render, redirect
import random

def index(request):
    if 'great' not in request.session:
        request.session['great'] = 0
    request.session['great'] = random.randint(1,100)
    print(request.session['great'])
    return render(request,'index.html')

def answer(request):
    user_input = request.POST['user_number']
    if int(user_input) == int(request.session['great']):
            return redirect('/correct')
    elif int(user_input) > int(request.session['great']):
            return redirect('/tooHigh')
    if int(user_input) < int(request.session['great']):
            return redirect('/tooLow')

def correct(request):
    return render(request, 'correct.html')

def tooHigh(request):
    return render(request, 'tooHigh.html')

def tooLow(request):
    return render(request, 'tooLow.html')

def tryAgain(request):
    return redirect('/')