from __future__ import unicode_literals
from django.db import models
from ..login_app.models import *
import os

# Notebook
class Category(models.Model):
    name = models.CharField(max_length=255)
    private = models.BooleanField(default=True)
    created_by = models.ForeignKey(User, related_name="categories")    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

# Category
class Subcategory(models.Model):
    name = models.CharField(max_length=255)
    private = models.BooleanField(default=True)
    parent = models.ForeignKey(Category, related_name="subcategories")
    created_by = models.ForeignKey(User, related_name="my_subcategories")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

# Note
class Note(models.Model):
    position_id = models.IntegerField(null=True)
    title = models.CharField(max_length=255)
    category = models.CharField(max_length=255)
    # parent = models.ForeignKey(Category, related_name="notes")
    content = models.TextField()
    private = models.BooleanField(default=False)
    created_by = models.ForeignKey(User, related_name="notes")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

# Comments
class NoteComment(models.Model):
    content = models.TextField()
    parent = models.ForeignKey(Note, related_name="subcontents")
    private = models.BooleanField(default=False)
    image = models.FileField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    isCode = models.BooleanField(default=False)
    # comments = models.ForeignKey(Note, related_name="comments")
    
    def extension(self):
        name, extension = os.path.splitext(self.image.name)
        return extension
        
class Document(models.Model):
    description = models.CharField(max_length=255, blank=True)
    document = models.FileField(upload_to='documents/')
    # parent = models.ForeignKey(NoteComment, related_name="documents")
    uploaded_at = models.DateTimeField(auto_now_add=True)