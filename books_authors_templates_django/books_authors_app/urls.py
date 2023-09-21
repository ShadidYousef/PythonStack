from django.urls import path
from . import views

urlpatterns = [
    path('', views.books),
    path('addBook', views.addBook),
    path('bookDetails/<int:bookID>', views.bookDetails),
    path('bookAdd/<int:bookID>', views.addAuthorToBook),
    path('authors', views.authors),
    path('addAuthor', views.addAuthor),
    path('authorDetails/<int:authorID>', views.authorDetails),
    path('authorAdd/<int:authorID>', views.addBooktoAuthor),
]