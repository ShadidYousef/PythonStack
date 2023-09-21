from django.db import models
from login_app.models import User

# Create your models here.
class Post(models.Model):
    user = models.ForeignKey(User, related_name="posts", on_delete=models.DO_NOTHING)
    post = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Comment(models.Model):
    post = models.ForeignKey(Post, related_name="comments", on_delete=models.CASCADE)
    user = models.ForeignKey(User, related_name="comments", on_delete=models.DO_NOTHING)
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

# write a new post and show it on the /wall page
def make_post_model(request):
    user = User.objects.get(id=request.session['userid'])
    post = request.POST['user_post']
    Post.objects.create(user = user, post = post)

# write a comment on a post
def make_comment_model(request, ID):
    user = User.objects.get(id = request.session['userid'])
    post = Post.objects.get(id = ID)
    comment = request.POST['user_comment']
    Comment.objects.create(post = post, user = user, comment = comment)
    
# get the logged in user session id
def user_session_model(request):
    return User.objects.get(id=request.session['userid'])

# get all posts to show on /wall and order them in decending order using their creation time
def get_posts_model():
    return Post.objects.all().order_by("-created_at")