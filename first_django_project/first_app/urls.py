from django.urls import path
from . import views

urlpatterns = [
    path('', views.root),
    path('blogs', views.index),
    path('blogs/new', views.new),
    path('create', views.create),
    path('blogs/<int:number>', views.show),
    path('blogs/<int:number>/edit', views.edit),
    path('blogs/<int:number>/delete', views.destroy),
    path('blogs/json', views.JsonMethod),
    path('empire', views.empire),
    # path('admin/', admin.site.urls),
]