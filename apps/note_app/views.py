from django.shortcuts import render, HttpResponse, redirect
from .models import *

def index(request):
    context = {
        'all_notes' : Note.objects.all(),
        'list_of_categories' : Category.objects.all(),
        'list_of_subcategories' : Subcategory.objects.all(),
        'list_of_note_comments': NoteComment.objects.all(),
    }
    return render(request, "note_app/index.html", context)

def add_note(request):
    Note.objects.create(title=request.POST['title'], category=request.POST['category'], content=request.POST['content'])
    return redirect('/')

def edit_note(request, note_id):
    
    return redirect('/')

def move_up(request, note_id):

    first_note_id = Note.objects.first().id
    upper_bound = first_note_id - 1
    print("Upper bound:" + str(upper_bound))

    last_note_id = Note.objects.last().id
    lower_bound = last_note_id + 1
    print("Lower bound:" + str(lower_bound))

    current_note = Note.objects.get(id=note_id)
    current_note_id = Note.objects.get(id=note_id).id

    prev_node_id = current_note_id - 1

    while(len(Note.objects.filter(id=prev_node_id)) == 0):
        prev_node_id = prev_node_id - 1

    prev_note = Note.objects.get(id=prev_node_id)

    print("Previous node id is: ", prev_note.id)
    print("Current node id is: ", current_note.id)
    
    temp = prev_note.id
    prev_note.id = current_note.id
    current_note.id = temp
    prev_note.save()
    current_note.save()
    
    return redirect('/')

def move_down(request, note_id):

    first_note_id = Note.objects.first().id
    upper_bound = first_note_id - 1
    print("Upper bound:" + str(upper_bound))

    last_note_id = Note.objects.last().id
    lower_bound = last_note_id + 1
    print("Lower bound:" + str(lower_bound))

    current_note = Note.objects.get(id=note_id)
    current_note_id = Note.objects.get(id=note_id).id

    prev_node_id = current_note_id + 1

    while(len(Note.objects.filter(id=prev_node_id)) == 0):
        prev_node_id = prev_node_id + 1

    prev_note = Note.objects.get(id=prev_node_id)

    print("Previous node id is: ", prev_note.id)
    print("Current node id is: ", current_note.id)
    
    temp = prev_note.id
    prev_note.id = current_note.id
    current_note.id = temp
    prev_note.save()
    current_note.save()
    
    return redirect('/')

def update_note(request, note_id):
    note_to_edit = Note.objects.get(id=note_id)
    note_to_edit.title = request.POST['title']
    note_to_edit.category = request.POST['category']
    note_to_edit.content = request.POST['content']
    note_to_edit.save()
    return redirect('/')

def delete_note(request, note_id):
    note_to_delete = Note.objects.get(id=note_id)
    note_to_delete.delete()
    return redirect('/')

def add_note_comment(request, note_id):
    print(request.POST['isCode'])
    parent = Note.objects.get(id=note_id)
    NoteComment.objects.create(content=request.POST['content'], parent=parent, isCode=request.POST['isCode'])
    return redirect('/')

def edit_note_comment(request, note_comment_id):
    note_comment_to_edit = NoteComment.objects.get(id=note_comment_id)
    note_comment_to_edit.content = request.POST['content']
    note_comment_to_edit.save()
    return redirect('/')

def delete_note_comment(request, note_comment_id):
    note_comment_to_delete = NoteComment.objects.get(id=note_comment_id)
    note_comment_to_delete.delete()
    return redirect('/')

def add_category(request):
    print("Creating a category")
    Category.objects.create(name=request.POST['name'])
    return redirect('/')

def add_subcategory(request, category_id):
    print("Creating a subcategory")
    Subcategory.objects.create(name=request.POST['name'], parent=Category.objects.get(id=category_id))
    return redirect('/')

def delete_subcategory(request, subcategory_id):
    subcategory_to_delete = Subcategory.objects.get(id=subcategory_id)
    subcategory_to_delete.delete()
    return redirect('/')

def view_subcategory(request, subcategory_name):
    print("Viewing page about ", subcategory_name)
    context = {
        'all_category_notes' : Note.objects.filter(category=subcategory_name),
        'subcategory_name' : subcategory_name,
    }
    return render(request, "note_app/view_subcategory.html", context)
    # return redirect('/')

def master_list(request):
    context = {
        'all_notes' : Note.objects.all(),
    }
    return render(request, "note_app/master_list.html", context)