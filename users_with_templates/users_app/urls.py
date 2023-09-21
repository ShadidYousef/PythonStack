from django.urls import path
from . import views
urlpatterns = [
    path('', views.index),
    path('addUser', views.addUser),
    path('deleteLast', views.deleteLast),
    path('deleteID/<int:x>', views.deleteID),
]