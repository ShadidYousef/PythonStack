from django.shortcuts import render, redirect
from .models import Users

def index(request):
    users = Users.objects.all()
    users_dict = {
        "users": users
    }
    return render(request, 'index.html', users_dict)
def addUser(request):
    first_name = request.POST['firstName']
    last_name = request.POST['lastName']
    email_address = request.POST['emailAddress']
    user_age = request.POST['userAge']
    Users.objects.create(first_name = first_name, last_name = last_name, email_address = email_address, age = user_age)
    return redirect('/')
def deleteLast(request):
    last_user = Users.objects.last()
    last_user.delete()
    return redirect('/')
def deleteID(request, x):
    user_id = Users.objects.get(id = x)
    user_id.delete()
    return redirect('/')