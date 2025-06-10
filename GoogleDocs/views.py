
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from .models import Document
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
def create_document(request):
    doc = Document.objects.create()
    return redirect('edit_document', doc_id=doc.id)
def edit_document(request, doc_id):
    doc = get_object_or_404(Document, id=doc_id)
    return render(request, 'Editing.html', {
        'documentTitle': doc.title,
        'doc': doc
    })