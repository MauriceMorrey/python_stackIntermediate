# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse, redirect, reverse
from .models import *
from django.contrib import messages
import bcrypt
# Create your views here.
def index(request):
    print User.objects.all()
    return render(request, 'login/index.html')

def register(request):
    errors = User.objects.basic_validator(request.POST)
    if len(errors):
        for error in errors:
            messages.error(request, errors[error])
        print errors
        return redirect("/")
    else:
        first_name = request.POST["first_name"]
        last_name = request.POST["last_name"]
        email = request.POST["email"]
        password = bcrypt.hashpw(request.POST['password'].encode(), bcrypt.gensalt())
        new_user = User.objects.create(first_name=first_name, last_name=last_name, email=email, password=password)
        print new_user
        request.session["username"] = first_name 
        request.session["user_id"] = new_user.id 
        return redirect("/")

def login(request):
    errors = User.objects.login_validator(request.POST)
    if len(errors):
        for error in errors:
            messages.error(request, errors[error])
        print errors
        return redirect("/")
    email = User.objects.get(email=request.POST["email"]) 
    # password = bcrypt.checkpw("request.POST['password']".encode(), email.password.encode())
    # password = User.objects.filter(email=request.POST["email"])[0].password
    if email == []:
		messages.error(request, "Invalid email or password.")
		return redirect("/")
    elif bcrypt.checkpw(request.POST['password'].encode(), email.password.encode()):
        print(request.POST['password'].encode())
        print("DB PASS!!!!",email.password.encode())
    # elif password == email.password:
        # return(True, email)
        request.session["username"] = email.first_name
        request.session["user_id"] = email.id
        return redirect("/belt")
    # elif not bcrypt.checkpw("request.POST['password']".encode(), password.encode()):
    #     messages.error(request, "Invalid email or password.")
    #     return redirect("/")
    else:
        messages.error(request, "Invalid email or password.")
        return redirect('/')

# def success(request):
#     return render(request, 'login/success.html')

def logout(request):
    request.session.clear()
    return redirect('/')