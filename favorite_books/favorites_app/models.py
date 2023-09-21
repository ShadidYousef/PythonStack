from django.db import models
from login_app.models import User
import re
import bcrypt

class Book(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(default="No description added, click Edit to add one now!")
    uploaded_by = models.ForeignKey(User, related_name="books_uploaded", on_delete=models.CASCADE)
    users_who_like = models.ManyToManyField(User, related_name="liked_books")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

# logged in user session
def user_session_model(request):
    return User.objects.get(id=request.session['userid'])

# get all books
def get_all_books_model():
    return Book.objects.all()

# create a new book and connect it's uploader and add this book to his liked books
def add_book_model(request):
    user = User.objects.get(id=request.session['userid'])
    book_title = request.POST['book_title']
    book_desc = request.POST['book_desc']
    new_book = Book.objects.create(title = book_title, description = book_desc, uploaded_by = user)
    user.liked_books.add(new_book)

# view a book info by id in the url
def view_book_model(request, ID):
    user = User.objects.get(id=request.session['userid'])
    book = Book.objects.get(id = ID)
    return user, book

def fav_book_model(request, ID):
    user = User.objects.get(id=request.session['userid'])
    book = Book.objects.get(id = ID)
    user.liked_books.add(book)

def unfav_book_model(request, ID):
    user = User.objects.get(id=request.session['userid'])
    book = Book.objects.get(id = ID)
    user.liked_books.remove(book)

def update_book_model(request):
    ID = request.POST['bookid']
    book = Book.objects.get(id = ID)
    input_title = request.POST['book_title']
    input_desc = request.POST['book_desc']
    book.title = input_title
    book.description = input_desc
    book.save()
    return ID

def delete_model(request):
    book = Book.objects.get(id = request.POST['delete_book'])
    book.delete()