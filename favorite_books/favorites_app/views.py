from django.shortcuts import render, redirect
from . import models
from .models import User, Book

def books(request):
    context = {
        "user": models.user_session_model(request),
        "books": models.get_all_books_model()
    }
    return render(request, 'books.html', context)
def add_book(request):
    models.add_book_model(request)
    return redirect('/books')

def view_book(request, ID):
    user = User.objects.get(id=request.session['userid'])
    book = Book.objects.get(id = ID)
    context = {
        "user": user,
        "books": models.get_all_books_model(),
        "book": book
    }
    return render(request, 'book_info.html', context)

def fav_book(request, ID):
    models.fav_book_model(request, ID)
    return redirect(request.META['HTTP_REFERER'])

def unfav_book(request, ID):
    models.unfav_book_model(request, ID)
    return redirect(request.META['HTTP_REFERER'])

def view_edit_book(request, ID):
    user = User.objects.get(id=request.session['userid'])
    book = Book.objects.get(id = ID)
    context = {
        "user": user,
        "books": models.get_all_books_model(),
        "book": book
    }
    return render(request, 'edit_book.html', context)

def update_book(request):
    ID = models.update_book_model(request)
    return redirect(f'/books/edit/{ID}')

def delete(request):
    models.delete_model(request)
    return redirect('/books')