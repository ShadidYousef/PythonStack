from django.urls import path
from . import views

urlpatterns = [
    path('', views.root),
    path('shows', views.shows),
    path('shows/new', views.renderAddShow),
    path('shows/create', views.addShow),
    path('shows/<int:showID>', views.showInfo),
    path('shows/<int:showID>/destroy', views.delete),
    path('shows/<int:showID>/edit', views.renderEditShow),
    path('shows/<int:showID>/update', views.update),
]