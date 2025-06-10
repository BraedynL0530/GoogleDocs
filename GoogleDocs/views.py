
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm

import GoogleDocs


# Create your views here.
def home(request):
    return render(request, 'Home.html',)
def register(response):
    form = UserCreationForm()
    if response.method == "POST":
        form = UserCreationForm(response.POST)
        if form.is_valid():
            form.save()
            return redirect("login")  # or another page

    return render(response, "register.html", {"form": form})
def Doc(request):
    return render(request, 'Editing.html',)