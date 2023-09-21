from django.db import models

# Database
class Validator(models.Manager):
    def basic_validator(self, post_data):
        errors = {}

        if len(post_data['showTitle']) < 2:
            errors['showTitle'] = "Title must be at least 2 characters"
        if len(post_data['showNetwork']) < 3:
            errors['showNetwork'] = "Network must be at least 3 characters"
        if len(post_data['showDesc']) < 10 and len(post_data['showDesc']) > 0 :
            errors['showDesc'] = "Description must be at least 10 characters"
        return errors
    
class Show(models.Model):
    network = models.CharField(max_length=20)
    title = models.CharField(max_length=255)
    release_date = models.DateField(auto_now=False, auto_now_add=False)
    desc = models.TextField(default="No Description Yet!")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = Validator()

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