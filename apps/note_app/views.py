from django.shortcuts import render, HttpResponse, redirect
from .models import *
from apps.login_app.models import User
from .forms import DocumentForm
from django.core.files.storage import FileSystemStorage

def index(request):
    if 'active_user' not in request.session:
        return redirect('/')

    active_user = User.objects.get(id=request.session['active_user'])

    if 'selected_category' not in request.session:
        all_notes = Note.objects.filter(created_by=active_user).order_by('position_id')
        request.session['selected_category'] = 'None'
        print("no category selected:", request.session['selected_category'])
    else:
        all_notes = Note.objects.filter(created_by=active_user, category=request.session['selected_category']).order_by('position_id')
        print("category selected!", request.session['selected_category'])

    if request.method == 'POST':
        print("Uploading a file...")
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/notes/')
    else:
        context = {
            'all_notes' : all_notes,
            'list_of_notebooks' : Notebook.objects.filter(created_by=active_user),
            'list_of_public_categories' : Notebook.objects.filter(privacy=False),
            'list_of_subcategories' : Category.objects.all(),
            'list_of_comments': Comment.objects.all(),
            'form' : DocumentForm(),
            'all_files' : Document.objects.all(),
            'current_user' : User.objects.get(id=request.session['active_user']),
        }
        return render(request, "note_app/index.html", context)

def view_notebook(request, category):
    active_user = User.objects.get(id=request.session['active_user'])

    context = {
        'all_notes' : Note.objects.filter(category=category).filter(created_by=active_user),
        'all_category_notes' : Note.objects.filter(category=category),
        'category' : category,
        'list_of_notebooks' : Notebook.objects.filter(created_by=active_user),
        'list_of_public_categories' : Notebook.objects.filter(privacy=False),
        'list_of_subcategories' : Category.objects.all(),
        'current_user' : User.objects.get(id=request.session['active_user']),
        'list_of_comments': Comment.objects.all(),
    }
    return render(request, "note_app/view_subcategory.html", context)

def all_notes_partial(request):
    active_user = User.objects.get(id=request.session['active_user'])
    context = {
        'all_notes' : Note.objects.filter(created_by=active_user).order_by('position_id'),
        'list_of_notebooks' : Notebook.objects.filter(created_by=active_user),
        'list_of_public_categories' : Notebook.objects.filter(privacy=False),
        'list_of_subcategories' : Category.objects.all(),
        'list_of_comments': Comment.objects.all(),
        'form' : DocumentForm(),
        'all_files' : Document.objects.all(),
        'current_user' : User.objects.get(id=request.session['active_user']),
    }
    return render(request, "note_app/note_partial.html", context)

def category_partial(request, category):
    if category == 'undefined':
        category = "None"
        request.session['selected_category'] = 'None'

    request.session['selected_category'] = category
    active_user = User.objects.get(id=request.session['active_user'])
    context = {
        'all_notes' : Note.objects.filter(created_by=active_user, category=category).order_by('position_id'),
        'list_of_notebooks' : Notebook.objects.filter(created_by=active_user),
        'list_of_public_categories' : Notebook.objects.filter(privacy=False),
        'list_of_subcategories' : Category.objects.all(),
        'list_of_comments': Comment.objects.all(),
        'category': category,
        'form' : DocumentForm(),
        'all_files' : Document.objects.all(),
        'current_user' : User.objects.get(id=request.session['active_user'])
    }
    return render(request, "note_app/category_partial.html", context)

def master_list(request):
    context = {
        'all_public_notes' : Note.objects.filter(privacy=False).order_by('title'),
        'current_user' : User.objects.get(id=request.session['active_user'])
    }
    return render(request, "note_app/master_list.html", context)

def add_note(request):
    print("add_note")
    new_note = Note.objects.create(title=request.POST['title'], category=request.POST['category'], created_by=User.objects.get(id=request.session['active_user']), content=request.POST['content'], privacy=request.POST['privacy'])
    new_note.position_id = new_note.id
    new_note.save()
    return redirect('/notes/')

def edit_note(request, note_id):
    print("edit_note")
    note_to_edit = Note.objects.get(id=note_id)
    note_to_edit.title = request.POST['title']
    note_to_edit.category = request.POST['category']
    note_to_edit.content = request.POST['content']
    note_to_edit.privacy = request.POST['privacy']
    note_to_edit.save()
    return redirect('/notes/')

def delete_note(request, note_id):
    print("delete_note")
    note_to_delete = Note.objects.get(id=note_id)
    note_to_delete.delete()
    return redirect('/notes/')

def add_comment(request, note_id):
    print("add_note_comment")
    if request.method == 'POST':
        if len(request.FILES) > 0:
            print("File provided!")
            parent = Note.objects.get(id=note_id)
            image = request.FILES['myfile']
            Comment.objects.create(content=request.POST['content'], parent=parent, isCode=request.POST['isCode'], image=image)
            return redirect('/notes/')
        else:
            print("No file provided!")
            parent = Note.objects.get(id=note_id)
            Comment.objects.create(content=request.POST['content'], parent=parent, isCode=request.POST['isCode'])
            return redirect('/notes/')

def edit_comment(request, note_comment_id):
    print("edit_comment")
    note_comment_to_edit = Comment.objects.get(id=note_comment_id)
    note_comment_to_edit.content = request.POST['content']
    note_comment_to_edit.save()
    return redirect('/notes/')

def delete_comment(request, note_comment_id):
    print("delete_comment")
    note_comment_to_delete = Comment.objects.get(id=note_comment_id)
    note_comment_to_delete.delete()
    return redirect('/notes/')

def add_notebook(request):
    print("add_notebook")
    category = Notebook.objects.create(name=request.POST['name'], created_by=User.objects.get(id=request.session['active_user']))
    Category.objects.create(name=request.POST['name'], parent=category, created_by=User.objects.get(id=request.session['active_user']))
    return redirect('/notes/')

def delete_category(request, category_id):
    print("delete_category")
    category_to_delete = Notebook.objects.get(id=category_id)
    category_to_delete.delete()
    return redirect('/notes/')

def togglePrivacy(request, notebook_id):
    print("privacyToggle")
    active_user = User.objects.get(id=request.session['active_user'])
    category = Notebook.objects.get(id=notebook_id)
    if category.privacy == True:
        print("False")
        category.privacy = False
        category.save()
    else:
        print("True")
        category.privacy = True
        category.save()
    return redirect('/notes/')

def add_subcategory(request, category_id):
    print("add_subcategory")
    Category.objects.create(name=request.POST['name'], parent=Notebook.objects.get(id=category_id), created_by=User.objects.get(id=request.session['active_user']))
    return redirect('/notes/')

def delete_subcategory(request, subcategory_id):
    print("delete_subcategory")
    subcategory_to_delete = Category.objects.get(id=subcategory_id)
    subcategory_to_delete.delete()
    return redirect('/notes/')

def drag_and_drop(request, starting_note_id, ending_note_id):

    starting_note = Note.objects.get(position_id=starting_note_id)
    ending_note = Note.objects.get(position_id=ending_note_id)

    starting_note.position_id = ending_note_id
    ending_note.position_id = starting_note_id

    starting_note.save()
    ending_note.save()
    return HttpResponse(200)