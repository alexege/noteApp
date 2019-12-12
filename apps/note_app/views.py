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
        request.session['selected_category'] = 'All'
        category = 'All'
        print("no category selected:", request.session['selected_category'])
    elif request.session['selected_category'] == 'All':
        print("selected_category was All")
        all_notes = Note.objects.filter(privacy=False).order_by('position_id')
        category = 'All'
    else:
        all_notes = Note.objects.filter(created_by=active_user, category=request.session['selected_category']).order_by('position_id')
        category = request.session['selected_category']
        print("category selected: ", request.session['selected_category'])

    if request.method == 'POST':
        print("Uploading a file...")
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/notes/')
    else:
        context = {
            'all_notes' : all_notes,
            'list_of_notebooks' : Notebook.objects.filter(created_by=active_user).order_by('position_id'),
            'list_of_public_notebooks' : Notebook.objects.filter(privacy=False),
            'list_of_categories' : Category.objects.all(),
            'list_of_comments': Comment.objects.all(),
            'category': category,
            'form' : DocumentForm(),
            'all_files' : Document.objects.all(),
            'current_user' : User.objects.get(id=request.session['active_user']),
            'active_user' : active_user
        }
        return render(request, "note_app/index.html", context)

def note_partial(request, category):
    request.session['selected_category'] = category
    active_user = User.objects.get(id=request.session['active_user'])

    if category == 'undefined':
        category = 'All'
        request.session['selected_category'] = 'All'
        all_notes = Note.objects.filter(created_by=active_user, privacy=False).order_by('position_id')
    elif category == 'All':
        all_notes = Note.objects.filter(created_by=active_user, privacy=False).order_by('position_id')
    elif category == 'alphabetical':
        all_notes = Note.objects.filter(created_by=active_user, privacy=False).order_by('title')
    elif category == 'date_added':
        all_notes = Note.objects.filter(created_by=active_user, privacy=False).order_by('created_at')
    else:
        all_notes = Note.objects.filter(created_by=active_user, category=category).order_by('position_id')
    
    print(request.session['selected_category'])

    context = {
        'all_notes' : all_notes,
        'list_of_notebooks' : Notebook.objects.filter(created_by=active_user),
        'list_of_public_categories' : Notebook.objects.filter(privacy=False),
        'list_of_categories' : Category.objects.all(),
        'list_of_comments': Comment.objects.all(),
        'category': category,
        'form' : DocumentForm(),
        'all_files' : Document.objects.all(),
        'current_user' : User.objects.get(id=request.session['active_user'])
    }
    return render(request, "note_app/note_partial.html", context)

def public_note_partial(request, category):
    request.session['selected_category'] = category
    active_user = User.objects.get(id=request.session['active_user'])

    if category == 'undefined':
        category = 'All'
        request.session['selected_category'] = 'All'
        all_notes = Note.objects.filter(privacy=False).order_by('position_id')
    elif category == 'All':
        all_notes = Note.objects.filter(privacy=False).order_by('position_id')
    else:
        all_notes = Note.objects.filter(category=category).order_by('position_id')

    print(request.session['selected_category'])

    context = {
        'all_notes' : all_notes,
        'list_of_notebooks' : Notebook.objects.filter(created_by=active_user),
        'list_of_public_categories' : Notebook.objects.filter(privacy=False),
        'list_of_categories' : Category.objects.all(),
        'list_of_comments': Comment.objects.all(),
        'category': category,
        'form' : DocumentForm(),
        'all_files' : Document.objects.all(),
        'current_user' : User.objects.get(id=request.session['active_user'])
    }
    return render(request, "note_app/note_partial.html", context)

def master_list(request):
    active_user = request.session['active_user']
    context = {
        'all_notes' : Note.objects.filter(created_by=active_user),
        'all_public_notes' : Note.objects.filter(privacy=False).order_by('title'),
        'current_user' : User.objects.get(id=request.session['active_user'])
    }
    return render(request, "note_app/master_list.html", context)

def add_note(request):
    category = request.session['selected_category']
    active_user = User.objects.get(id=request.session['active_user'])

    if category == 'undefined':
        category = 'All'
        request.session['selected_category'] = 'All'
        all_notes = Note.objects.filter(privacy=False).order_by('position_id')
    elif category == 'All':
        all_notes = Note.objects.filter(privacy=False).order_by('position_id')
    else:
        all_notes = Note.objects.filter(created_by=active_user, category=category).order_by('position_id')

    new_note = Note.objects.create(title=request.POST['title'], category=request.POST['category'], created_by=User.objects.get(id=request.session['active_user']), content=request.POST['content'], privacy=request.POST['privacy'])
    new_note.position_id = new_note.id
    new_note.save()

    context = {
        'all_notes' : all_notes,
        'list_of_notebooks' : Notebook.objects.filter(created_by=active_user),
        'list_of_public_categories' : Notebook.objects.filter(privacy=False),
        'list_of_categories' : Category.objects.all(),
        'list_of_comments': Comment.objects.all(),
        'category': category,
        'form' : DocumentForm(),
        'all_files' : Document.objects.all(),
        'current_user' : User.objects.get(id=request.session['active_user'])
    }
    return render(request, "note_app/note_partial.html", context)


def edit_note(request, note_id):
    print("edit_note")
    note_to_edit = Note.objects.get(id=note_id)
    note_to_edit.title = request.POST['title']
    note_to_edit.category = request.POST['category']
    note_to_edit.content = request.POST['content']
    note_to_edit.privacy = request.POST['privacy']
    note_to_edit.save()
    # return redirect('/notes/')

    category = request.session['selected_category']
    active_user = User.objects.get(id=request.session['active_user'])
    print("Category is: [" + category + "]")
    if category == 'undefined':
        category = 'All'
        request.session['selected_category'] = 'All'
        all_notes = Note.objects.filter(privacy=False).order_by('position_id')
        print("-------undefined--------")
    elif category == 'All':
        all_notes = Note.objects.filter(privacy=False).order_by('position_id')
        print("-------All--------")
    else:
        print("-------else--------")
        all_notes = Note.objects.filter(created_by=active_user, category=category).order_by('position_id')

    context = {
        'all_notes' : all_notes,
        'list_of_notebooks' : Notebook.objects.filter(created_by=active_user),
        'list_of_public_categories' : Notebook.objects.filter(privacy=False),
        'list_of_categories' : Category.objects.all(),
        'list_of_comments': Comment.objects.all(),
        'category': category,
        'form' : DocumentForm(),
        'all_files' : Document.objects.all(),
        'current_user' : User.objects.get(id=request.session['active_user'])
    }
    return render(request, "note_app/note_partial.html", context)

def delete_note(request, note_id):
    print("delete_note")
    note_to_delete = Note.objects.get(id=note_id)
    note_to_delete.delete()
    # return redirect('/notes/')

    category = request.session['selected_category']
    active_user = User.objects.get(id=request.session['active_user'])
    print("Category is: [" + category + "]")
    if category == 'undefined':
        category = 'All'
        request.session['selected_category'] = 'All'
        all_notes = Note.objects.filter(privacy=False).order_by('position_id')
        print("-------undefined--------")
    elif category == 'All':
        all_notes = Note.objects.filter(privacy=False).order_by('position_id')
        print("-------All--------")
    else:
        print("-------else--------")
        all_notes = Note.objects.filter(created_by=active_user, category=category).order_by('position_id')

    context = {
        'all_notes' : all_notes,
        'list_of_notebooks' : Notebook.objects.filter(created_by=active_user),
        'list_of_public_categories' : Notebook.objects.filter(privacy=False),
        'list_of_categories' : Category.objects.all(),
        'list_of_comments': Comment.objects.all(),
        'category': category,
        'form' : DocumentForm(),
        'all_files' : Document.objects.all(),
        'current_user' : User.objects.get(id=request.session['active_user'])
    }
    return render(request, "note_app/note_partial.html", context)


def add_comment(request, note_id):
    print("add_note_comment")
    print("request.FILES:", request.FILES)
    if request.method == 'POST':
        category = request.session['selected_category']
        active_user = User.objects.get(id=request.session['active_user'])

        if category == 'undefined':
            category = 'All'
            request.session['selected_category'] = 'All'
            all_notes = Note.objects.filter(privacy=False).order_by('position_id')
        elif category == 'All':
            all_notes = Note.objects.filter(privacy=False).order_by('position_id')
        else:
            all_notes = Note.objects.filter(created_by=active_user, category=category).order_by('position_id')

        if len(request.FILES) > 0:
            print("File provided!")
            parent = Note.objects.get(id=note_id)
            image = request.FILES['myfile']
            Comment.objects.create(content=request.POST['content'], parent=parent, isCode=request.POST['isCode'], image=image)
            # return redirect('/notes/')
            context = {
                'all_notes' : all_notes,
                'list_of_notebooks' : Notebook.objects.filter(created_by=active_user),
                'list_of_public_categories' : Notebook.objects.filter(privacy=False),
                'list_of_categories' : Category.objects.all(),
                'list_of_comments': Comment.objects.all(),
                'category': category,
                'form' : DocumentForm(),
                'all_files' : Document.objects.all(),
                'current_user' : User.objects.get(id=request.session['active_user'])
            }
            return render(request, "note_app/note_partial.html", context)
        else:
            print("No file provided!")
            parent = Note.objects.get(id=note_id)
            Comment.objects.create(content=request.POST['content'], parent=parent, isCode=request.POST['isCode'])
            # return redirect('/notes/')
            context = {
                'all_notes' : all_notes,
                'list_of_notebooks' : Notebook.objects.filter(created_by=active_user),
                'list_of_public_categories' : Notebook.objects.filter(privacy=False),
                'list_of_categories' : Category.objects.all(),
                'list_of_comments': Comment.objects.all(),
                'category': category,
                'form' : DocumentForm(),
                'all_files' : Document.objects.all(),
                'current_user' : User.objects.get(id=request.session['active_user'])
            }
            return render(request, "note_app/note_partial.html", context)


def edit_comment(request, note_comment_id):
    print("edit_comment")
    note_comment_to_edit = Comment.objects.get(id=note_comment_id)
    note_comment_to_edit.content = request.POST['content']
    note_comment_to_edit.isCode = request.POST['isCode']
    note_comment_to_edit.save()
    # return redirect('/notes/')

    category = request.session['selected_category']
    active_user = User.objects.get(id=request.session['active_user'])
    print("Category is: [" + category + "]")
    if category == 'undefined':
        category = 'All'
        request.session['selected_category'] = 'All'
        all_notes = Note.objects.filter(privacy=False).order_by('position_id')
        print("-------undefined--------")
    elif category == 'All':
        all_notes = Note.objects.filter(privacy=False).order_by('position_id')
        print("-------All--------")
    else:
        print("-------else--------")
        all_notes = Note.objects.filter(created_by=active_user, category=category).order_by('position_id')

    context = {
        'all_notes' : all_notes,
        'list_of_notebooks' : Notebook.objects.filter(created_by=active_user),
        'list_of_public_categories' : Notebook.objects.filter(privacy=False),
        'list_of_categories' : Category.objects.all(),
        'list_of_comments': Comment.objects.all(),
        'category': category,
        'form' : DocumentForm(),
        'all_files' : Document.objects.all(),
        'current_user' : User.objects.get(id=request.session['active_user'])
    }
    return render(request, "note_app/note_partial.html", context)

def delete_comment(request, note_comment_id):
    note_comment_to_delete = Comment.objects.get(id=note_comment_id)
    note_comment_to_delete.delete()
    # return redirect('/notes/')

    category = request.session['selected_category']
    active_user = User.objects.get(id=request.session['active_user'])

    if category == 'undefined':
        category = 'All'
        request.session['selected_category'] = 'All'
        all_notes = Note.objects.filter(privacy=False).order_by('position_id')
    elif category == 'All':
        all_notes = Note.objects.filter(privacy=False).order_by('position_id')
    else:
        all_notes = Note.objects.filter(created_by=active_user, category=category).order_by('position_id')

    context = {
        'all_notes' : all_notes,
        'list_of_notebooks' : Notebook.objects.filter(created_by=active_user),
        'list_of_public_categories' : Notebook.objects.filter(privacy=False),
        'list_of_categories' : Category.objects.all(),
        'list_of_comments': Comment.objects.all(),
        'category': category,
        'form' : DocumentForm(),
        'all_files' : Document.objects.all(),
        'current_user' : User.objects.get(id=request.session['active_user'])
    }
    return render(request, "note_app/note_partial.html", context)

def indent_comment(request, comment_id):
    comment = Comment.objects.get(id=comment_id)
    comment.indentLevel += 1
    comment.save()
    
    category = request.session['selected_category']
    active_user = User.objects.get(id=request.session['active_user'])

    if category == 'undefined':
        category = 'All'
        request.session['selected_category'] = 'All'
        all_notes = Note.objects.filter(privacy=False).order_by('position_id')
    elif category == 'All':
        all_notes = Note.objects.filter(privacy=False).order_by('position_id')
    else:
        all_notes = Note.objects.filter(created_by=active_user, category=category).order_by('position_id')

    context = {
        'all_notes' : all_notes,
        'list_of_notebooks' : Notebook.objects.filter(created_by=active_user),
        'list_of_public_categories' : Notebook.objects.filter(privacy=False),
        'list_of_categories' : Category.objects.all(),
        'list_of_comments': Comment.objects.all(),
        'category': category,
        'form' : DocumentForm(),
        'all_files' : Document.objects.all(),
        'current_user' : User.objects.get(id=request.session['active_user'])
    }
    return render(request, "note_app/note_partial.html", context)

def outdent_comment(request, comment_id):
    comment = Comment.objects.get(id=comment_id)
    if comment.indentLevel > 0:
        comment.indentLevel -= 1
    comment.save()
    
    category = request.session['selected_category']
    active_user = User.objects.get(id=request.session['active_user'])

    if category == 'undefined':
        category = 'All'
        request.session['selected_category'] = 'All'
        all_notes = Note.objects.filter(privacy=False).order_by('position_id')
    elif category == 'All':
        all_notes = Note.objects.filter(privacy=False).order_by('position_id')
    else:
        all_notes = Note.objects.filter(created_by=active_user, category=category).order_by('position_id')

    context = {
        'all_notes' : all_notes,
        'list_of_notebooks' : Notebook.objects.filter(created_by=active_user),
        'list_of_public_categories' : Notebook.objects.filter(privacy=False),
        'list_of_categories' : Category.objects.all(),
        'list_of_comments': Comment.objects.all(),
        'category': category,
        'form' : DocumentForm(),
        'all_files' : Document.objects.all(),
        'current_user' : User.objects.get(id=request.session['active_user'])
    }
    return render(request, "note_app/note_partial.html", context)

def add_notebook(request):
    print("add_notebook")
    notebook = Notebook.objects.create(name=request.POST['name'], created_by=User.objects.get(id=request.session['active_user']))
    Category.objects.create(name=request.POST['name'], parent=notebook, created_by=User.objects.get(id=request.session['active_user']))
    
    notebook.position_id = notebook.id
    notebook.save()

    active_user = User.objects.get(id=request.session['active_user'])

    context = {
        'active_user': active_user,
        'list_of_public_notebooks' : Notebook.objects.filter(privacy=False),
        'list_of_categories' : Category.objects.all(),
        'list_of_notebooks' : Notebook.objects.filter(created_by=active_user).order_by('position_id'),
        'current_user' : User.objects.get(id=request.session['active_user'])
    }
    
    return render(request, "note_app/sidenav_partial.html", context)
    # return redirect('/notes/')

def edit_notebook(request, notebook_id):
    print("edit_notebook")
    notebook = Notebook.objects.get(id=notebook_id)
    notebook.name = request.POST['name']
    notebook.save()

    active_user = User.objects.get(id=request.session['active_user'])

    context = {
        'active_user': active_user,
        'list_of_public_notebooks' : Notebook.objects.filter(privacy=False),
        'list_of_categories' : Category.objects.all(),
        'list_of_notebooks' : Notebook.objects.filter(created_by=active_user).order_by('position_id'),
        'current_user' : User.objects.get(id=request.session['active_user'])
    }
    
    return render(request, "note_app/sidenav_partial.html", context)

def delete_notebook(request, notebook_id):
    print("delete_notebook")
    category_to_delete = Notebook.objects.get(id=notebook_id)
    category_to_delete.delete()

    active_user = User.objects.get(id=request.session['active_user'])

    context = {
        'active_user': active_user,
        'list_of_public_notebooks' : Notebook.objects.filter(privacy=False),
        'list_of_categories' : Category.objects.all(),
        'list_of_notebooks' : Notebook.objects.filter(created_by=active_user).order_by('position_id'),
        'current_user' : User.objects.get(id=request.session['active_user'])
    }
    
    return render(request, "note_app/sidenav_partial.html", context)

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
    # return redirect('/notes/')
    context = {
        'active_user': active_user,
        'list_of_notebooks' : Notebook.objects.filter(created_by=active_user).order_by('position_id'),
        'list_of_public_notebooks' : Notebook.objects.filter(privacy=False),
        'list_of_categories' : Category.objects.all(),
        'current_user' : User.objects.get(id=request.session['active_user'])
    }
    return render(request, "note_app/sidenav_partial.html", context)

def add_category(request, category_id):
    print("add_category")
    Category.objects.create(name=request.POST['name'], parent=Notebook.objects.get(id=category_id), created_by=User.objects.get(id=request.session['active_user']))
    # return redirect('/notes/')
    active_user = User.objects.get(id=request.session['active_user'])

    context = {
        'active_user': active_user,
        'list_of_notebooks' : Notebook.objects.filter(created_by=active_user).order_by('position_id'),
        'list_of_public_notebooks' : Notebook.objects.filter(privacy=False),
        'list_of_categories' : Category.objects.all(),
        'current_user' : User.objects.get(id=request.session['active_user'])
    }
    return render(request, "note_app/sidenav_partial.html", context)

def delete_category(request, category_id):
    print("delete_category")
    category_to_delete = Category.objects.get(id=category_id)
    category_to_delete.delete()
    
    active_user = User.objects.get(id=request.session['active_user'])

    context = {
        'active_user': active_user,
        'list_of_notebooks' : Notebook.objects.filter(created_by=active_user).order_by('position_id'),
        'list_of_public_notebooks' : Notebook.objects.filter(privacy=False),
        'list_of_categories' : Category.objects.all(),
        'current_user' : User.objects.get(id=request.session['active_user'])
    }
    return render(request, "note_app/sidenav_partial.html", context)
    
def drag_and_drop(request, starting_note_id, ending_note_id):

    starting_note = Note.objects.get(position_id=starting_note_id)
    ending_note = Note.objects.get(position_id=ending_note_id)

    starting_note.position_id = ending_note_id
    ending_note.position_id = starting_note_id

    starting_note.save()
    ending_note.save()
    return HttpResponse(200)
    
def drag_and_drop_notebook(request, starting_notebook_id, ending_notebook_id):
    starting_notebook = Notebook.objects.get(position_id=starting_notebook_id)
    ending_notebook = Notebook.objects.get(position_id=ending_notebook_id)

    starting_notebook.position_id = ending_notebook_id
    ending_notebook.position_id = starting_notebook_id

    starting_notebook.save()
    ending_notebook.save()
    return HttpResponse(200)