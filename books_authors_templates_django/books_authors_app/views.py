from django.shortcuts import render, redirect, HttpResponse
from . import models

# books
def books(request):
    context = {
        "BOOKS": models.getBook(request),
    }
    return render(request, 'books.html', context)

def addBook(request):
    models.createBook(request)
    return redirect('/')

def bookDetails(request, bookID):
    context = {
        "BOOKS": models.getBook(request),
        "BOOK_INFO": models.getBookInfo(bookID),
        "AUTHORS": models.getAuthor(request)
    }
    return render(request, 'book_details.html', context)

def addAuthorToBook(request, bookID):
    models.connectAuthorToBook(request, bookID)
    return redirect(request.META['HTTP_REFERER']) 


# -------------------------------------


# authors
def authors(request):
    context = {
        "AUTHORS": models.getAuthor(request)
    }
    return render(request, 'authors.html', context)

def addAuthor(request):
    models.createAuthor(request)
    return redirect('/authors')

def authorDetails(request, authorID):
    context = {
        "AUTHORS": models.getAuthor(request),
        "AUTHOR_INFO": models.getAuthorInfo(request, authorID),
        "BOOKS": models.getBook(request)
    }
    return render(request, 'author_details.html', context)

def addBooktoAuthor(request, authorID):
    models.connectBookToAuthor(request, authorID)
    return redirect('/authors')

def deleteBook(request, authorID):
    models.disconnectBook(request, authorID)
    return redirect(request.META['HTTP_REFERER'])