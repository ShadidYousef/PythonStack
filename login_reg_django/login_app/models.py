from django.db import models
from django.shortcuts import redirect
import re
import bcrypt

class Validator(models.Manager):
    def basic_validator(self, post_data):
        errors = {}
        # db_emails = User.objects.get(email = post_data['email'])
        # if post_data["email"] == db_emails.email:
        #     errors['email'] = "This Email is already in use!"
        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        if not EMAIL_REGEX.match(post_data['email']):
            errors['email'] = "Invalid email address!"
        PASSWORD_REGEX = re.compile(r'^[a-zA-Z0-9.@+_-]+$')
        if not PASSWORD_REGEX.match(post_data['password']):
            errors['password'] = "Password cannot contain these characters!"
        FIRSTNAME_REGEX = re.compile(r'^[a-zA-Z]+$')
        if not FIRSTNAME_REGEX.match(post_data['first_name']):
            errors['first_name'] = "Name must be in alphabetical letters only!"
        LASTNAME_REGEX = re.compile(r'^[a-zA-Z]+$')
        if not LASTNAME_REGEX.match(post_data['last_name']):
            errors['last_name'] = "Name must be in alphabetical letters only!"
        if len(post_data['first_name']) < 2:
            errors['first_name'] = "First Name must be at least 2 characters"
        if len(post_data['last_name']) < 2:
            errors['last_name'] = "Last Name must be at least 2 characters"
        if len(post_data['password']) < 10 :
            errors['password'] = "Password must be at least 8 characters"
        if post_data['password'] != post_data['confirm_password'] :
            errors['confirm_password'] = "Your password didn't match!"
        
        
        return errors

class User(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField(max_length=254)
    password = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = Validator()

def register_model(request):
    first_name = request.POST['first_name']
    last_name = request.POST['last_name']
    email = request.POST['email']
    password = request.POST['password']
    password_hash = bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()
    User.objects.create(first_name = first_name, last_name = last_name, email = email, password = password_hash)
    user = User.objects.filter(email=request.POST['email'])
    logged_user = user[0]
    request.session['userid'] = logged_user.id
    return redirect('/success')
    

def login_model(request):
    user = User.objects.filter(email=request.POST['email']) 
    if user:
        logged_user = user[0]
        if bcrypt.checkpw(request.POST['log_password'].encode(), logged_user.password.encode()):
            request.session['userid'] = logged_user.id
            return redirect('/success')
    return redirect('/')

def user_session_model(request):
    return User.objects.get(id=request.session['userid'])
