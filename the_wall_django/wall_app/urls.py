from django.urls import path
from . import views

urlpatterns = [
    path('wall', views.wall),
    path('makepost', views.make_post),
    path('makecomment/<int:ID>', views.make_comment),
    path('delete_post', views.delete_post)
]