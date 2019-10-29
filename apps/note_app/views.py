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

    # current_note = Note.objects.get(id=note_id)

    # id_of_next_node = int(note_id) + 1
    # last_node_exist = Note.objects.filter(id=id_of_next_node)
    # print("LAST NODE EXIST: ", last_node_exist)

    # #If last note exists
    # if(last_node_exist):
    #     last_note = Note.objects.get(id=id_of_next_node)
    #     temp = last_note.id
    #     last_note.id = current_note.id
    #     current_note.id = temp
    #     last_note.save()
    #     current_note.save()
    
    return redirect('/')

def update_note(request, note_id):
    note_to_edit = Note.objects.get(id=note_id)
    note_to_edit.title = request.POST['title']
    note_to_edit.category = request.POST['category']
    note_to_edit.content = request.POST['content']
    return redirect('/')

def delete_note(request, note_id):
    note_to_delete = Note.objects.get(id=note_id)
    note_to_delete.delete()
    return redirect('/')