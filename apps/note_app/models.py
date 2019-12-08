from __future__ import unicode_literals
from django.db import models
from ..login_app.models import *
import os

class Notebook(models.Model):
    name = models.CharField(max_length=255)
    privacy = models.BooleanField(default=True)
    created_by = models.ForeignKey(User, related_name="categories")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Category(models.Model):
    name = models.CharField(max_length=255)
    privacy = models.BooleanField(default=True)
    parent = models.ForeignKey(Notebook, related_name="subcategories")
    created_by = models.ForeignKey(User, related_name="my_subcategories")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Note(models.Model):
    position_id = models.IntegerField(null=True)
    title = models.CharField(max_length=255)
    category = models.CharField(max_length=255)
    content = models.TextField()
    privacy = models.BooleanField(default=False)
    created_by = models.ForeignKey(User, related_name="notes")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Comment(models.Model):
    content = models.TextField()
    parent = models.ForeignKey(Note, related_name="subcontents")
    privacy = models.BooleanField(default=False)
    image = models.FileField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    isCode = models.BooleanField(default=False)
    indentLevel = models.IntegerField(default=0)
    
    def extension(self):
        name, extension = os.path.splitext(self.image.name)
        return extension
        
class Document(models.Model):
    description = models.CharField(max_length=255, blank=True)
    document = models.FileField(upload_to='documents/')
    uploaded_at = models.DateTimeField(auto_now_add=True)