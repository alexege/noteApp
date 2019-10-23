from django.shortcuts import render, HttpResponse, redirect
from .models import *

def index(request):
    context = {
        'all_notes' : Note.objects.all(),
        'list_of_categories' : Category.objects.all()
    }
    return render(request, "note_app/index.html", context)

def add_note(request):
    Note.objects.create(title=request.POST['title'], category=request.POST['category'], content=request.POST['content'])
    return redirect('/')