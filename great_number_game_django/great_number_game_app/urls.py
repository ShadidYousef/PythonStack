from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('answer', views.answer),
    path('correct', views.correct),
    path('tooHigh', views.tooHigh),
    path('tooLow', views.tooLow),
    path('reset', views.tryAgain),
]