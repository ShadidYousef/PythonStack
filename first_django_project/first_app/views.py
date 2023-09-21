from django.shortcuts import render, redirect, HttpResponse
from django.http import JsonResponse

def root(request):
    return redirect('/blogs')
def index(request):
    return HttpResponse('placeholder to later display a list of all blogs')
def new(request):
    return HttpResponse('placeholder to display a new form to create a new blog')
def create(request):
    return redirect('/')
def show(request, number):
    return HttpResponse(f'placeholder to display the blog number {number}')
def edit(request, number):
    return HttpResponse(f'placeholder to edit blog {number}')
def destroy(request, number):
    return redirect('/blogs')
# Bonus answer!
def JsonMethod(request):
    my_dict = {
        "name": "Muath",
        "age": 27,
        "job": "Studying Full Stack Development"
    }
    return JsonResponse(my_dict, safe=False)
# Experiment!!
def empire(request):
    empire_name = {
        "name": "Sparta",
        "age": 2722
    }
    return render(request, 'index.html', empire_name)