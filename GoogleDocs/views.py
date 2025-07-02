import os

from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST

from DocsClone import settings
from .models import Document
import GoogleDocs
from django.http import JsonResponse, HttpResponseForbidden, HttpResponse
import json

# Create your views here.
@login_required
def home(request):
    try:
        shared_docs = request.user.shared_docs.all()
    except Exception as e:
        shared_docs = Document.objects.none()  # fallback to empty
        print("SHARED_DOCS ERROR:", e)

    owned_docs = Document.objects.filter(owner=request.user)
    shared_docs = request.user.shared_docs.all()  # related_name='shared_docs' from your model

    documents = owned_docs | shared_docs  # combine both querysets
    documents = documents.distinct().order_by('-created_at')

    return render(request, 'Home.html', {'documents': documents})
def register(response):
    form = UserCreationForm()
    if response.method == "POST":
        form = UserCreationForm(response.POST)
        if form.is_valid():
            form.save()
            return redirect("login")  # or another page

    return render(response, "register.html", {"form": form})
def create_document(request):
    if not request.user.is_authenticated:
        return redirect('login')

    doc = Document.objects.create(owner=request.user)
    return redirect('edit_document', doc_id=doc.id)
@login_required
def edit_document(request, doc_id):
    doc = get_object_or_404(Document, id=doc_id)
    if request.user != doc.owner and request.user not in doc.shared_with.all():
        return HttpResponseForbidden()

    return render(request, 'Editing.html', {
        'documentTitle': doc.title,
        'doc': doc
    })

@require_POST
def update_title(request, doc_id):
    if request.method == 'POST':
        data = json.loads(request.body)
        doc = Document.objects.get(id=doc_id)
        doc.title = data['title']
        doc.save()
        return JsonResponse({'status': 'ok'})


@require_POST
def update_content(request, doc_id):
    data = json.loads(request.body)
    doc = Document.objects.get(id=doc_id)
    doc.content = data['content']
    doc.save()
    return JsonResponse({'status': 'saved'})
@require_POST
def share_document(request, doc_id):
    doc = get_object_or_404(Document, id=doc_id)

    if doc.owner != request.user:
        return HttpResponseForbidden("Only the owner can share this document.")

    data = json.loads(request.body)
    username = data.get('username')

    try:
        user_to_share = User.objects.get(username=username)
        doc.shared_with.add(user_to_share)
        return JsonResponse({'status': 'shared'})
    except User.DoesNotExist:
        return JsonResponse({'status': 'error', 'message': 'User not found'}, status=404)


def check_template(request):
    template_path = os.path.join(settings.BASE_DIR, 'templates', 'home.html')
    exists = os.path.exists(template_path)
    return HttpResponse(f"Template exists? {exists} at {template_path}")