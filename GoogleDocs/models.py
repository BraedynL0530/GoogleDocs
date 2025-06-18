from django.contrib.auth.models import User
from django.db import models
# Create your models here.
from django.db import models
import uuid

class Document(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=200, default='Untitled document')
    content = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='documents',null=True,blank=True)
    shared_with = models.ManyToManyField(User, related_name='shared_docs', blank=True)