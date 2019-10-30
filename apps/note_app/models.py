from django.db import models

class Note(models.Model):
    title = models.CharField(max_length=255)
    category = models.CharField(max_length=255)
    content = models.TextField()
    private = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class NoteComment(models.Model):
    content = models.TextField()
    parent = models.ForeignKey(Note, related_name="subcontents")
    private = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    # comments = models.ForeignKey(Note, related_name="comments")

class Category(models.Model):
    name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Subcategory(models.Model):
    name = models.CharField(max_length=255)
    parent = models.ForeignKey(Category, related_name="subcategories")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
        