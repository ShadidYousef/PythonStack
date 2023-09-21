from django.shortcuts import render, redirect
from login_app.models import User
from .models import Post, Comment
from . import models

def make_post(request):
    models.make_post_model(request)
    return redirect('/wall')

def make_comment(request, ID):
    models.make_comment_model(request, ID)
    return redirect('/wall')

# render the wall.html page on the browser
def wall(request):
    context = {
        "user": models.user_session_model(request),
        "posts": models.get_posts_model(),
        # "comments": Comment.objects.all().order_by("-created_at")
    }
    return render(request, 'wall.html', context)

# delete a post but only if you're the creator of this certain post
def delete_post(request):
    post = Post.objects.get(id = request.POST['delete_post'])
    user = User.objects.get(id = request.session['userid'])
    if user.id == post.user.id:
        post.delete()
        return redirect('/wall')
    else:
        return redirect('/wall')