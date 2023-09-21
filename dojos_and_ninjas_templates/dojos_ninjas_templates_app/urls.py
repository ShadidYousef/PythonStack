from django.urls import path
from . import views
urlpatterns = [
    path('', views.index),
    path('addDojo', views.dojo),
    path('addNinja', views.ninja),
    path('deleteDojo/<int:dojo_id>', views.deleteDojo),
]
