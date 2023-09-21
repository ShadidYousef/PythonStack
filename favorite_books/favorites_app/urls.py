from django.urls import path
from . import views

urlpatterns = [
  path('books', views.books),
  path('add_book', views.add_book),
  path('books/<int:ID>', views.view_book),
  path('fav_book/<int:ID>', views.fav_book),
  path('unfav_book/<int:ID>', views.unfav_book),
  path('books/edit/<int:ID>', views.view_edit_book),
  path('books/update', views.update_book),
  path('books/delete', views.delete),
  

]