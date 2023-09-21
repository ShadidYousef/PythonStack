from django.db import models
# Database
class Show(models.Model):
    network = models.CharField(max_length=20)
    title = models.CharField(max_length=255)
    release_date = models.DateField(auto_now=False, auto_now_add=False)
    desc = models.TextField(default="No Description Yet!")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

# -------------------------------------

# Shows
def addShow_model(request):
    add_show = Show.objects.create(network = request.POST['showNetwork'], title = request.POST['showTitle'], release_date = request.POST['showReleaseDate'], desc = request.POST['showDesc'])
    return add_show
def getShows_model(request):
    shows = Show.objects.all()
    return shows
def getShowInfo_model(request, showID):
    SHOW_INFO = Show.objects.get(id = showID)
    return SHOW_INFO
def delete_model(request, showID):
    show = Show.objects.get(id = showID)
    delete_show = show.delete()
    return delete_show
def update_model(request, showID):
    show = Show.objects.get(id = showID)
    show.title = request.POST['showTitle']
    show.network = request.POST['showNetwork']
    show.release_date = request.POST['showReleaseDate']
    show.desc = request.POST['showDesc']
    show_update = show.save()
    return show_update