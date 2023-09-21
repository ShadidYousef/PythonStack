from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('register', views.register),
    # path('success', views.success),
    path('login', views.login),
    path('logout', views.logout),
    # path('wall', wall_app.views.wall),
    # path('makepost', wall_app.views.make_post)
]