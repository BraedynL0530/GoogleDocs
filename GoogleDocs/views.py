
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.views.decorators.csrf import csrf_exempt

from .models import Document
import GoogleDocs
from django.http import JsonResponse
import json

# Create your views here.
def home(request):
    documents = Document.objects.order_by('-created_at')#Recent docs, for now by create date :c
    return render(request, 'home.html', {'documents': documents})
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

@csrf_exempt
def update_title(request, doc_id):
    if request.method == 'POST':
        data = json.loads(request.body)
        doc = Document.objects.get(id=doc_id)
        doc.title = data['title']
        doc.save()
        return JsonResponse({'status': 'ok'})