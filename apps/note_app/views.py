from django.shortcuts import render, HttpResponse, redirect
from .models import *
from apps.login_app.models import User
from .forms import DocumentForm
from django.core.files.storage import FileSystemStorage

def index(request):

    if 'active_user' not in request.session:
        return redirect('/')

    if 'selected_notebook' not in request.session:
        print("selected_notebook not found")
        request.session['selected_notebook'] = 'All'
    
    if 'selected_category' not in request.session:
        print("selected_category not found")
        request.session['selected_category'] = 'All'

    active_user = User.objects.get(id=request.session['active_user'])

    # If All notebook doesn't exist, create it
    if len(Notebook.objects.filter(name='All')) < 1:
        notebook = Notebook.objects.create(name='All', created_by=User.objects.get(id=request.session['active_user']))
        notebook.position_id = notebook.id
        notebook.save()
        Category.objects.create(name='All', parent=notebook, created_by=active_user)

    for key, value in request.session.items():
        print('{} => {}'.format(key, value))

    notebook = Notebook.objects.get(name=request.session['selected_notebook'])
    category = Category.objects.get(name=request.session['selected_category'], parent=notebook)

    print("Notebook:", notebook.name)
    print("Category:", category.name)

    if notebook.name == 'All' and category.name == 'All':
        print("Displaying everything")
        all_notes = Note.objects.filter(created_by=active_user).order_by('position_id')
    else:
        all_notes = Note.objects.filter(created_by=active_user, parent=notebook, category=category).order_by('position_id')

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
            'category': category.name,
            'form' : DocumentForm(),
            'all_files' : Document.objects.all(),
            'current_user' : User.objects.get(id=request.session['active_user']),
            'active_user' : active_user
        }
        return render(request, "note_app/index.html", context)

def note_partial(request, notebook, category):

    if notebook == 'default' and category == 'default':
        notebook = request.session['selected_notebook']
        category = request.session['selected_category']

    if 'active_user' not in request.session:
        request.session['active_user'] = User.objects.get(id=request.session['active_user'])
        return redirect('/')

    if 'selected_notebook' not in request.session:
        request.session['selected_notebook'] = 'All'
    
    if 'selected_category' not in request.session:
        request.session['selected_category'] = 'All'

    print("notebook:", notebook)
    print("category:", category)
    # notebook = Notebook.objects.get(name=notebook)
    # category = Category.objects.get(name=category)

    request.session['selected_notebook'] = notebook
    request.session['selected_category'] = category

    notebook = Notebook.objects.get(name=request.session['selected_notebook'])
    category = Category.objects.get(name=request.session['selected_category'], parent=notebook)
    active_user = User.objects.get(id=request.session['active_user'])

    if notebook.name == 'All' and category.name == 'All':
        all_notes = Note.objects.filter(created_by=active_user).order_by('position_id')
    else:
        all_notes = Note.objects.filter(created_by=active_user, parent=notebook, category=category).order_by('position_id')
    
    context = {
        'all_notes' : all_notes,
        'list_of_notebooks' : Notebook.objects.filter(created_by=active_user),
        'list_of_public_categories' : Notebook.objects.filter(privacy=False),
        'list_of_categories' : Category.objects.all(),
        'list_of_comments': Comment.objects.all(),
        'category': category.name,
        'form' : DocumentForm(),
        'all_files' : Document.objects.all(),
        'current_user' : User.objects.get(id=request.session['active_user'])
    }
    return render(request, "note_app/note_partial.html", context)

# def view_sidenav(request):
#     print("Viewing sidenav")

#     notebook = Notebook.objects.get(name=request.session['selected_notebook'])
#     category = Category.objects.get(name=request.session['selected_category'])
#     active_user = User.objects.get(id=request.session['active_user'])

#     all_notes = Note.objects.filter(created_by=active_user, parent=notebook, category=category).order_by('position_id')
#     print("all_notes:", all_notes)
#     print("Notebook:", notebook.name)
#     print("Category:", category.name)

#     context = {
#         'all_notes' : all_notes,
#         'list_of_notebooks' : Notebook.objects.filter(created_by=active_user),
#         'list_of_public_categories' : Notebook.objects.filter(privacy=False),
#         'list_of_categories' : Category.objects.all(),
#         'list_of_comments': Comment.objects.all(),
#         'category': 'view_sidenav',
#         'form' : DocumentForm(),
#         'all_files' : Document.objects.all(),
#         'current_user' : User.objects.get(id=request.session['active_user'])
#     }
#     return render(request, 'note_app/sidenav_partial.html', context)

def all_notebook_categories(request, notebook_name):
    if 'active_user' not in request.session:
        request.session['active_user'] = User.objects.get(id=request.session['active_user'])
        return redirect('/')

    if 'selected_notebook' not in request.session:
        request.session['selected_notebook'] = 'All'
    
    if 'selected_category' not in request.session:
        request.session['selected_category'] = 'All'

    notebook = Notebook.objects.get(name=request.session['selected_notebook'])
    category = Category.objects.get(name=request.session['selected_category'], parent=notebook)
    active_user = User.objects.get(id=request.session['active_user'])

    all_notes = Note.objects.filter(created_by=active_user, parent=notebook).order_by('position_id')

    print(request.session['selected_category'])

    context = {
        'all_notes' : all_notes,
        'list_of_notebooks' : Notebook.objects.filter(created_by=active_user),
        'list_of_public_categories' : Notebook.objects.filter(privacy=False),
        'list_of_categories' : Category.objects.all(),
        'list_of_comments': Comment.objects.all(),
        'category': 'all_notebook_categories',
        'form' : DocumentForm(),
        'all_files' : Document.objects.all(),
        'current_user' : User.objects.get(id=request.session['active_user'])
    }
    return render(request, "note_app/note_partial.html", context)

def all_my_notes(request):

    if 'active_user' not in request.session:
        request.session['active_user'] = User.objects.get(id=request.session['active_user'])
        return redirect('/')

    if 'selected_notebook' not in request.session:
        request.session['selected_notebook'] = 'All'
    
    if 'selected_category' not in request.session:
        request.session['selected_category'] = 'All'

    notebook = Notebook.objects.get(name=request.session['selected_notebook'])
    category = Category.objects.get(name=request.session['selected_category'], parent=notebook)
    active_user = User.objects.get(id=request.session['active_user'])

    all_notes = Note.objects.filter(created_by=active_user).order_by('position_id')

    print(request.session['selected_category'])

    context = {
        'all_notes' : all_notes,
        'list_of_notebooks' : Notebook.objects.filter(created_by=active_user),
        'list_of_public_categories' : Notebook.objects.filter(privacy=False),
        'list_of_categories' : Category.objects.all(),
        'list_of_comments': Comment.objects.all(),
        'category': 'all_my_notes',
        'form' : DocumentForm(),
        'all_files' : Document.objects.all(),
        'current_user' : User.objects.get(id=request.session['active_user'])
    }
    return render(request, "note_app/note_partial.html", context)

def public_note_partial(request, notebook, category):
    request.session['selected_notebook'] = notebook
    request.session['selected_category'] = category

    if 'active_user' not in request.session:
        request.session['active_user'] = User.objects.get(id=request.session['active_user'])
        return redirect('/')

    if 'selected_notebook' not in request.session:
        request.session['selected_notebook'] = 'All'
    
    if 'selected_category' not in request.session:
        request.session['selected_category'] = 'All'

    notebook = Notebook.objects.get(name=request.session['selected_notebook'])
    category = Category.objects.get(name=request.session['selected_category'], parent=notebook)
    active_user = User.objects.get(id=request.session['active_user'])

    all_notes = Note.objects.filter(parent=notebook, category=category).order_by('position_id')
    context = {
        'all_notes' : all_notes,
        'list_of_notebooks' : Notebook.objects.filter(created_by=active_user),
        'list_of_public_categories' : Notebook.objects.filter(privacy=False),
        'list_of_categories' : Category.objects.all(),
        'list_of_comments': Comment.objects.all(),
        'category': 'public_note_partial',
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

def add_note(request, notebook_name):

    if 'active_user' not in request.session:
        request.session['active_user'] = User.objects.get(id=request.session['active_user'])
        return redirect('/')

    if 'selected_notebook' not in request.session:
        request.session['selected_notebook'] = 'All'
    
    if 'selected_category' not in request.session:
        request.session['selected_category'] = 'All'

    notebook = Notebook.objects.get(name=request.session['selected_notebook'])
    category = Category.objects.get(name=request.session['selected_category'], parent=notebook)
    active_user = User.objects.get(id=request.session['active_user'])

    print("Notebook:", notebook.name)
    print("Category:", category.name)

    if notebook.name == 'All' and category.name == 'All':
        all_notes = Note.objects.filter(created_by=active_user).order_by('position_id')
    else:
        all_notes = Note.objects.filter(created_by=active_user, parent=notebook, category=category).order_by('position_id')

    new_note = Note.objects.create(title=request.POST['title'] ,parent=notebook, category=category, created_by=active_user, content=request.POST['content'], privacy=request.POST['privacy'])
    new_note.position_id = new_note.id
    new_note.save()

    context = {
        'all_notes' : all_notes,
        'list_of_notebooks' : Notebook.objects.filter(created_by=active_user),
        'list_of_public_categories' : Notebook.objects.filter(privacy=False),
        'list_of_categories' : Category.objects.all(),
        'list_of_comments': Comment.objects.all(),
        'category': 'add_note',
        'form' : DocumentForm(),
        'all_files' : Document.objects.all(),
        'current_user' : User.objects.get(id=request.session['active_user'])
    }
    return render(request, "note_app/note_partial.html", context)


def edit_note(request, note_id):
    print("edit_note")
    note_to_edit = Note.objects.get(id=note_id)
    note_to_edit.title = request.POST['title']
    note_to_edit.category = Category.objects.get(name=request.POST['category'])
    note_to_edit.content = request.POST['content']
    # note_to_edit.privacy = request.POST['privacy']
    note_to_edit.save()

    if 'active_user' not in request.session:
        return redirect('/')

    if 'selected_notebook' not in request.session:
        request.session['selected_notebook'] = 'All'
    
    if 'selected_category' not in request.session:
        request.session['selected_category'] = 'All'

    notebook = Notebook.objects.get(name=request.session['selected_notebook'])
    category = Category.objects.get(name=request.session['selected_category'])
    active_user = User.objects.get(id=request.session['active_user'])

    all_notes = Note.objects.filter(created_by=active_user, parent=notebook, category=category).order_by('position_id')

    context = {
        'all_notes' : all_notes,
        'list_of_notebooks' : Notebook.objects.filter(created_by=active_user),
        'list_of_public_categories' : Notebook.objects.filter(privacy=False),
        'list_of_categories' : Category.objects.all(),
        'list_of_comments': Comment.objects.all(),
        'category': 'edit_note',
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

    if 'active_user' not in request.session:
        return redirect('/')

    if 'selected_notebook' not in request.session:
        request.session['selected_notebook'] = 'All'
    
    if 'selected_category' not in request.session:
        request.session['selected_category'] = 'All'

    notebook = Notebook.objects.get(name=request.session['selected_notebook'])
    category = Category.objects.get(name=request.session['selected_category'])
    active_user = User.objects.get(id=request.session['active_user'])

    all_notes = Note.objects.filter(created_by=active_user, parent=notebook, category=category).order_by('position_id')

    context = {
        'all_notes' : all_notes,
        'list_of_notebooks' : Notebook.objects.filter(created_by=active_user),
        'list_of_public_categories' : Notebook.objects.filter(privacy=False),
        'list_of_categories' : Category.objects.all(),
        'list_of_comments': Comment.objects.all(),
        'category': 'delete_note',
        'form' : DocumentForm(),
        'all_files' : Document.objects.all(),
        'current_user' : User.objects.get(id=request.session['active_user'])
    }
    return render(request, "note_app/note_partial.html", context)

from django.views.decorators.csrf import csrf_exempt
@csrf_exempt
def add_comment(request, note_id):

    if request.method == 'POST':
        if 'active_user' not in request.session:
            return redirect('/')

        if 'selected_notebook' not in request.session:
            request.session['selected_notebook'] = 'All'
        
        if 'selected_category' not in request.session:
            request.session['selected_category'] = 'All'

        notebook = Notebook.objects.get(name=request.session['selected_notebook'])
        category = Category.objects.get(name=request.session['selected_category'], parent=notebook)
        active_user = User.objects.get(id=request.session['active_user'])

        all_notes = Note.objects.filter(created_by=active_user, parent=notebook, category=category).order_by('position_id')

        # print("Content:", request.POST['content'])

        if len(request.FILES) > 0:
            print("File provided!")
            parent = Note.objects.get(id=note_id)
            image = request.FILES['myfile']
            Comment.objects.create(content=request.POST['content'], parent=parent, container=request.POST['container'], image=image, bullet=request.POST['bullet'])
        else:
            print("No file provided!")
            parent = Note.objects.get(id=note_id)
            comment = Comment.objects.create(content=request.POST['content'], parent=parent, container=request.POST['container'], bullet=request.POST['bullet'])

        context = {
            'all_notes' : all_notes,
            'list_of_notebooks' : Notebook.objects.filter(created_by=active_user),
            'list_of_public_categories' : Notebook.objects.filter(privacy=False),
            'list_of_categories' : Category.objects.all(),
            'list_of_comments': Comment.objects.all(),
            'category': 'adding_comment_with_or_without_file',
            'form' : DocumentForm(),
            'all_files' : Document.objects.all(),
            'current_user' : User.objects.get(id=request.session['active_user'])
        }
        return render(request, "note_app/note_partial.html", context)


def edit_comment(request, comment_id):
    print("edit_comment")
    note_comment_to_edit = Comment.objects.get(id=comment_id)
    note_comment_to_edit.content = request.POST['content']
    note_comment_to_edit.container = request.POST['container']
    note_comment_to_edit.save()
    # return redirect('/notes/')

    if 'active_user' not in request.session:
        return redirect('/')

    if 'selected_notebook' not in request.session:
        request.session['selected_notebook'] = 'All'
    
    if 'selected_category' not in request.session:
        request.session['selected_category'] = 'All'

    notebook = Notebook.objects.get(name=request.session['selected_notebook'])
    category = Category.objects.get(name=request.session['selected_category'], parent=notebook)
    active_user = User.objects.get(id=request.session['active_user'])

    all_notes = Note.objects.filter(created_by=active_user, parent=notebook, category=category).order_by('position_id')

    context = {
        'all_notes' : all_notes,
        'list_of_notebooks' : Notebook.objects.filter(created_by=active_user),
        'list_of_public_categories' : Notebook.objects.filter(privacy=False),
        'list_of_categories' : Category.objects.all(),
        'list_of_comments': Comment.objects.all(),
        'category': 'edit_comment',
        'form' : DocumentForm(),
        'all_files' : Document.objects.all(),
        'current_user' : User.objects.get(id=request.session['active_user'])
    }
    return render(request, "note_app/note_partial.html", context)

def toggle_comment_bullet(request, comment_id, bullet_style):
    print("toggling bullet")

    comment_to_edit = Comment.objects.get(id=comment_id)
    comment_to_edit.bullet = bullet_style
    comment_to_edit.save()
    print("Comment to edit:", comment_to_edit.bullet)

    if 'active_user' not in request.session:
        return redirect('/')

    if 'selected_notebook' not in request.session:
        request.session['selected_notebook'] = 'All'
    
    if 'selected_category' not in request.session:
        request.session['selected_category'] = 'All'

    notebook = Notebook.objects.get(name=request.session['selected_notebook'])
    category = Category.objects.get(name=request.session['selected_category'], parent=notebook)
    active_user = User.objects.get(id=request.session['active_user'])

    all_notes = Note.objects.filter(created_by=active_user, parent=notebook, category=category).order_by('position_id')

    context = {
        'all_notes' : all_notes,
        'list_of_notebooks' : Notebook.objects.filter(created_by=active_user),
        'list_of_public_categories' : Notebook.objects.filter(privacy=False),
        'list_of_categories' : Category.objects.all(),
        'list_of_comments': Comment.objects.all(),
        'category': 'edit_comment',
        'form' : DocumentForm(),
        'all_files' : Document.objects.all(),
        'current_user' : User.objects.get(id=request.session['active_user'])
    }
    return render(request, "note_app/note_partial.html", context)

def delete_comment(request, note_comment_id):
    note_comment_to_delete = Comment.objects.get(id=note_comment_id)
    note_comment_to_delete.delete()

    if 'active_user' not in request.session:
        return redirect('/')

    if 'selected_notebook' not in request.session:
        request.session['selected_notebook'] = 'All'
    
    if 'selected_category' not in request.session:
        request.session['selected_category'] = 'All'

    notebook = Notebook.objects.get(name=request.session['selected_notebook'])
    category = Category.objects.get(name=request.session['selected_category'], parent=notebook)
    active_user = User.objects.get(id=request.session['active_user'])

    all_notes = Note.objects.filter(created_by=active_user, parent=notebook, category=category).order_by('position_id')

    context = {
        'all_notes' : all_notes,
        'list_of_notebooks' : Notebook.objects.filter(created_by=active_user),
        'list_of_public_categories' : Notebook.objects.filter(privacy=False),
        'list_of_categories' : Category.objects.all(),
        'list_of_comments': Comment.objects.all(),
        'category': 'delete_comment',
        'form' : DocumentForm(),
        'all_files' : Document.objects.all(),
        'current_user' : User.objects.get(id=request.session['active_user'])
    }
    return render(request, "note_app/note_partial.html", context)

def indent_comment(request, comment_id):
    comment = Comment.objects.get(id=comment_id)
    comment.indentLevel += 1
    comment.save()
    
    if 'active_user' not in request.session:
        return redirect('/')

    if 'selected_notebook' not in request.session:
        request.session['selected_notebook'] = 'All'
    
    if 'selected_category' not in request.session:
        request.session['selected_category'] = 'All'

    notebook = Notebook.objects.get(name=request.session['selected_notebook'])
    category = Category.objects.get(name=request.session['selected_category'], parent=notebook)
    active_user = User.objects.get(id=request.session['active_user'])

    all_notes = Note.objects.filter(created_by=active_user, parent=notebook, category=category).order_by('position_id')

    context = {
        'all_notes' : all_notes,
        'list_of_notebooks' : Notebook.objects.filter(created_by=active_user),
        'list_of_public_categories' : Notebook.objects.filter(privacy=False),
        'list_of_categories' : Category.objects.all(),
        'list_of_comments': Comment.objects.all(),
        'category': 'indent_comment',
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
    
    if 'active_user' not in request.session:
        return redirect('/')

    if 'selected_notebook' not in request.session:
        request.session['selected_notebook'] = 'All'
    
    if 'selected_category' not in request.session:
        request.session['selected_category'] = 'All'

    notebook = Notebook.objects.get(name=request.session['selected_notebook'])
    category = Category.objects.get(name=request.session['selected_category'], parent=notebook)
    active_user = User.objects.get(id=request.session['active_user'])

    all_notes = Note.objects.filter(created_by=active_user, parent=notebook, category=category).order_by('position_id')

    context = {
        'all_notes' : all_notes,
        'list_of_notebooks' : Notebook.objects.filter(created_by=active_user),
        'list_of_public_categories' : Notebook.objects.filter(privacy=False),
        'list_of_categories' : Category.objects.all(),
        'list_of_comments': Comment.objects.all(),
        'category': 'outdent_comment',
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

    #If a category is deleted, reset default view
    request.session['selected_notebook'] = 'All'
    request.session['selected_category'] = 'All'
    
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