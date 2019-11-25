from django.shortcuts import render, HttpResponse, redirect
from .models import *
from apps.login_app.models import User
from .forms import DocumentForm
from django.core.files.storage import FileSystemStorage

def index(request):
    print("Request Method", request.method)
    if 'active_user' not in request.session:
        return redirect('/')

    if request.method == 'POST':
        print("Uploading a file...")
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/notes/')
    else:
        active_user = User.objects.get(id=request.session['active_user'])
        context = {
            'all_notes' : Note.objects.filter(created_by=active_user).order_by('position_id'),
            # 'all_notes' : Note.objects.filter(isPublic=true),
            # 'list_of_categories' : Category.objects.filter(creator=active_user),
            'list_of_categories' : Category.objects.filter(created_by=active_user),
            'list_of_public_categories' : Category.objects.filter(private=False),
            'list_of_subcategories' : Subcategory.objects.all(),
            'list_of_note_comments': NoteComment.objects.all(),
            'form' : DocumentForm(),
            'all_files' : Document.objects.all(),
            'current_user' : User.objects.get(id=request.session['active_user'])
        }
        return render(request, "note_app/index.html", context)

def all_notes_partial(request):
    active_user = User.objects.get(id=request.session['active_user'])
    context = {
        'all_notes' : Note.objects.filter(created_by=active_user).order_by('position_id'),
        'list_of_categories' : Category.objects.filter(created_by=active_user),
        'list_of_public_categories' : Category.objects.filter(private=False),
        'list_of_subcategories' : Subcategory.objects.all(),
        'list_of_note_comments': NoteComment.objects.all(),
        'form' : DocumentForm(),
        'all_files' : Document.objects.all(),
        'current_user' : User.objects.get(id=request.session['active_user'])
    }
    return render(request, "note_app/note_partial.html", context)

def add_note(request):
    print("add_note")
    new_note = Note.objects.create(title=request.POST['title'], category=request.POST['category'], created_by=User.objects.get(id=request.session['active_user']), content=request.POST['content'], private=request.POST['privacy'])
    new_note.position_id = new_note.id
    new_note.save()
    return redirect('/notes/')

def edit_note(request, note_id):
    print("edit_note")
    note_to_edit = Note.objects.get(id=note_id)
    note_to_edit.title = request.POST['title']
    note_to_edit.category = request.POST['category']
    note_to_edit.content = request.POST['content']
    note_to_edit.private = request.POST['privacy']
    note_to_edit.save()
    return redirect('/notes/')

def move_up(request, note_id):
    print("move_up")

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
    
    return redirect('/notes/')

def move_down(request, note_id):
    print("move_down")
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
    
    return redirect('/notes/')

def update_note(request, note_id):
    print("update_note")
    note_to_edit = Note.objects.get(id=note_id)
    note_to_edit.title = request.POST['title']
    note_to_edit.category = request.POST['category']
    note_to_edit.content = request.POST['content']
    note_to_edit.save()
    return redirect('/notes/')

def delete_note(request, note_id):
    print("delete_note")
    note_to_delete = Note.objects.get(id=note_id)
    note_to_delete.delete()
    return redirect('/notes/')

def add_note_comment(request, note_id):
    print("add_note_comment")
    if request.method == 'POST':
        print("Length:", len(request.FILES))
        if len(request.FILES) > 0:
            print("File provided!")
            parent = Note.objects.get(id=note_id)
            image = request.FILES['myfile']
            NoteComment.objects.create(content=request.POST['content'], parent=parent, isCode=request.POST['isCode'], image=image)
            return redirect('/notes/')
        else:
            print("No file provided!")
            parent = Note.objects.get(id=note_id)
            NoteComment.objects.create(content=request.POST['content'], parent=parent, isCode=request.POST['isCode'])
            return redirect('/notes/')

def edit_note_comment(request, note_comment_id):
    print("edit_note_comment")
    note_comment_to_edit = NoteComment.objects.get(id=note_comment_id)
    note_comment_to_edit.content = request.POST['content']
    note_comment_to_edit.save()
    return redirect('/notes/')

def delete_note_comment(request, note_comment_id):
    print("delete_note_comment")
    note_comment_to_delete = NoteComment.objects.get(id=note_comment_id)
    note_comment_to_delete.delete()
    return redirect('/notes/')

def add_notebook(request):
    print("add_notebook")
    category = Category.objects.create(name=request.POST['name'], created_by=User.objects.get(id=request.session['active_user']))
    Subcategory.objects.create(name=request.POST['name'], parent=category, created_by=User.objects.get(id=request.session['active_user']))
    return redirect('/notes/')

def add_subcategory(request, category_id):
    print("add_subcategory")
    Subcategory.objects.create(name=request.POST['name'], parent=Category.objects.get(id=category_id), created_by=User.objects.get(id=request.session['active_user']))
    return redirect('/notes/')

def privacyToggle(request, category_id):
    print("privacyToggle")
    category = Category.objects.get(id=category_id)
    if category.private == True:
        print("False")
        category.private = False
        category.save()
    else:
        print("True")
        category.private = True
        category.save()
    return redirect('/notes/')

def categoryPrivacyToggle(request, category_id):
    print("privacyToggle")
    category = Category.objects.get(id=category_id)
    category_name = category.name
    # subcategory = Subcategory.objects.get(id=)
    if category.private == True:
        print("False")
        category.private = False
        category.save()
    else:
        print("True")
        category.private = True
        category.save()
    # return redirect('/notes/' + category_name)
    return redirect('/notes/category/view/' + category_name + '/' + str(category.id))

def delete_category(request, category_id):
    print("delete_category")
    category_to_delete = Category.objects.get(id=category_id)
    category_to_delete.delete()
    return redirect('/notes/')

def delete_subcategory(request, subcategory_id):
    print("delete_subcategory")
    subcategory_to_delete = Subcategory.objects.get(id=subcategory_id)
    subcategory_to_delete.delete()
    return redirect('/notes/')

def view_subcategory(request, category, subcategory_id):
    active_user = User.objects.get(id=request.session['active_user'])

    # category = request.POST['category']
    # subcategory = request.POST['subcategory']
    subcategory = Subcategory.objects.get(id=subcategory_id)
    context = {
        'all_notes' : Note.objects.filter(category=category).filter(created_by=active_user),
        'all_category_notes' : Note.objects.filter(category=subcategory.name),
        'category' : category,
        'subcategory' : subcategory,
        'list_of_categories' : Category.objects.filter(created_by=active_user),
        'list_of_public_categories' : Category.objects.filter(private=False),
        'list_of_subcategories' : Subcategory.objects.all(),
        'current_user' : User.objects.get(id=request.session['active_user']),
        'list_of_note_comments': NoteComment.objects.all(),
    }
    return render(request, "note_app/view_subcategory.html", context)

def view_category(request, category):
    active_user = User.objects.get(id=request.session['active_user'])

    # category = request.POST['category']
    # subcategory = request.POST['subcategory']
    context = {
        'all_notes' : Note.objects.filter(category=category).filter(created_by=active_user),
        'all_category_notes' : Note.objects.filter(category=category),
        'category' : category,
        'list_of_categories' : Category.objects.filter(created_by=active_user),
        'list_of_public_categories' : Category.objects.filter(private=False),
        'list_of_subcategories' : Subcategory.objects.all(),
        'current_user' : User.objects.get(id=request.session['active_user']),
        'list_of_note_comments': NoteComment.objects.all(),
    }
    return render(request, "note_app/view_subcategory.html", context)

def add_note_from_category(request):
    print("add_note_from_category")
    category = request.POST['category']
    subcategory = request.POST['subcategory']
    # subcategory = Subcategory.objects.get(id=request.POST['subcategory']).id
    Note.objects.create(title=request.POST['title'], category=request.POST['category'], private=request.POST['privacy'], content=request.POST['content'], created_by=User.objects.get(id=request.session['active_user']))
    return redirect('/notes/category/view/' + category + "/" + str(subcategory))

def add_note_comment_from_category(request, note_id):
    print("add_note_comment_from_category")
    if request.method == 'POST':
        category = request.POST['category']
        subcategory = request.POST['subcategory']
        print(category)
        print(subcategory)
        print("Length:", len(request.FILES))
        if len(request.FILES) > 0:
            print("File provided!")
            parent = Note.objects.get(id=note_id)
            image = request.FILES['myfile']
            NoteComment.objects.create(content=request.POST['content'], parent=parent, isCode=request.POST['isCode'], image=image)
            return redirect('/notes/category/view/' + category + "/" + str(subcategory))
        else:
            print("No file provided!")
            parent = Note.objects.get(id=note_id)
            NoteComment.objects.create(content=request.POST['content'], parent=parent, isCode=request.POST['isCode'])
            return redirect('/notes/category/view/' + category + "/" + str(subcategory))
    return redirect('/notes/')

def delete_note_from_category(request, subcategory_id, note_id):
    print("delete_note")
    category = Note.objects.get(id=note_id).id
    note_to_delete = Note.objects.get(id=note_id)
    note_to_delete.delete()
    return redirect('/notes/category/view/' + str(category) + '/' + subcategory_id)

def delete_note_comment_from_category(request, note_comment_id, category, subcategory):
    print("delete_note_comment_from_category")
    note_comment_to_delete = NoteComment.objects.get(id=note_comment_id)
    note_comment_to_delete.delete()
    return redirect('/notes/category/view/' + category + "/" + subcategory)

def master_list(request):
    context = {
        'all_public_notes' : Note.objects.filter(private=False).order_by('title'),
        'current_user' : User.objects.get(id=request.session['active_user'])
    }
    return render(request, "note_app/master_list.html", context)

def drag_and_drop(request, starting_note_id, ending_note_id):

    starting_note = Note.objects.get(position_id=starting_note_id)
    ending_note = Note.objects.get(position_id=ending_note_id)

    starting_note.position_id = ending_note_id
    ending_note.position_id = starting_note_id

    starting_note.save()
    ending_note.save()
    return HttpResponse(200)