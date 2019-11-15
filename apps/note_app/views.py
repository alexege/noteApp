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
        'all_notes' : Note.objects.all(),
        # 'all_notes' : Note.objects.filter(isPublic=true),
        # 'list_of_categories' : Category.objects.filter(creator=active_user),
        'list_of_categories' : Category.objects.all(),
        'list_of_public_categories' : Subcategory.objects.filter(private=False),
        'list_of_subcategories' : Subcategory.objects.all(),
        'list_of_note_comments': NoteComment.objects.all(),
        'form' : DocumentForm(),
        'all_files' : Document.objects.all(),
        'current_user' : User.objects.get(id=request.session['active_user'])
    }
    return render(request, "note_app/index.html", context)

def add_note(request):
    Note.objects.create(title=request.POST['title'], category=request.POST['category'], created_by=User.objects.get(id=request.session['active_user']), content=request.POST['content'], private=request.POST['privacy'])
    return redirect('/notes/')

def edit_note(request, note_id):
    
    return redirect('/notes/')

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
    
    return redirect('/notes/')

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
    
    return redirect('/notes/')

def update_note(request, note_id):
    note_to_edit = Note.objects.get(id=note_id)
    note_to_edit.title = request.POST['title']
    note_to_edit.category = request.POST['category']
    note_to_edit.content = request.POST['content']
    note_to_edit.save()
    return redirect('/notes/')

def delete_note(request, note_id):
    note_to_delete = Note.objects.get(id=note_id)
    note_to_delete.delete()
    return redirect('/notes/')

def add_note_comment(request, note_id):
    if request.method == 'POST':
        print("Length:", len(request.FILES))
        if len(request.FILES) > 0:
            print("File provided!")
            parent = Note.objects.get(id=note_id)
            image = request.FILES['myfile']
            NoteComment.objects.create(content=request.POST['content'], parent=parent, isCode=request.POST['isCode'], image=image)
            # return redirect('/notes/')
            context = {
                'all_notes' : Note.objects.all(),
                # 'all_notes' : Note.objects.filter(isPublic=true),
                # 'list_of_categories' : Category.objects.filter(creator=active_user),
                'list_of_categories' : Category.objects.all(),
                'list_of_public_categories' : Subcategory.objects.filter(private=False),
                'list_of_subcategories' : Subcategory.objects.all(),
                'list_of_note_comments': NoteComment.objects.all(),
                'form' : DocumentForm(),
                'all_files' : Document.objects.all(),
                'current_user' : User.objects.get(id=request.session['active_user'])
            }
            return render(request, "note_app/note_comment.html", context)
        else:
            print("No file provided!")
            parent = Note.objects.get(id=note_id)
            NoteComment.objects.create(content=request.POST['content'], parent=parent, isCode=request.POST['isCode'])
            # return redirect('/notes/')
            context = {
                'all_notes' : Note.objects.all(),
                # 'all_notes' : Note.objects.filter(isPublic=true),
                # 'list_of_categories' : Category.objects.filter(creator=active_user),
                'list_of_categories' : Category.objects.all(),
                'list_of_public_categories' : Subcategory.objects.filter(private=False),
                'list_of_subcategories' : Subcategory.objects.all(),
                'list_of_note_comments': NoteComment.objects.all(),
                'form' : DocumentForm(),
                'all_files' : Document.objects.all(),
                'current_user' : User.objects.get(id=request.session['active_user'])
                }
    return render(request, "note_app/note_comment.html", context)

# def add_note_comment(request, note_id):
#     if request.method == 'POST':
#         print("Length:", len(request.FILES))
#         if len(request.FILES) > 0:
#             print("File provided!")
#             parent = Note.objects.get(id=note_id)
#             image = request.FILES['myfile']
#             NoteComment.objects.create(content=request.POST['content'], parent=parent, isCode=request.POST['isCode'], image=image)
#             return redirect('/notes/')
#         else:
#             print("No file provided!")
#             parent = Note.objects.get(id=note_id)
#             NoteComment.objects.create(content=request.POST['content'], parent=parent, isCode=request.POST['isCode'])
#             return redirect('/notes/')
#     return redirect('/notes/')

def edit_note_comment(request, note_comment_id):
    note_comment_to_edit = NoteComment.objects.get(id=note_comment_id)
    note_comment_to_edit.content = request.POST['content']
    note_comment_to_edit.save()
    return redirect('/notes/')

def delete_note_comment(request, note_comment_id):
    note_comment_to_delete = NoteComment.objects.get(id=note_comment_id)
    note_comment_to_delete.delete()
    return redirect('/notes/')

def add_category(request):
    print("Creating a category")
    category = Category.objects.create(name=request.POST['name'], created_by=User.objects.get(id=request.session['active_user']))
    Subcategory.objects.create(name=request.POST['name'], parent=category, created_by=User.objects.get(id=request.session['active_user']))
    return redirect('/notes/')

def add_subcategory(request, category_id):
    print("Creating a subcategory")
    Subcategory.objects.create(name=request.POST['name'], parent=Category.objects.get(id=category_id), created_by=User.objects.get(id=request.session['active_user']))
    return redirect('/notes/')

def privacyToggle(request, subcat_id):
    subcategory = Subcategory.objects.get(id=subcat_id)
    if subcategory.private == True:
        print("False")
        subcategory.private = False
        subcategory.save()
    else:
        print("True")
        subcategory.private = True
        subcategory.save()
    return redirect('/notes/')

# def privacyToggleCategory(request, cat_id):
#     category = Category.objects.get(id=cat_id)
#     if category.private == True:
#         # print("False")
#         category.private = False
#         print("The current state is: " , category.private)
#         category.save()
#     else:
#         # print("True")
#         category.private = True
#         category.save()
#         print("The current state is: " , category.private)
#     return redirect('/notes/')

def delete_subcategory(request, subcategory_id):
    subcategory_to_delete = Subcategory.objects.get(id=subcategory_id)
    subcategory_to_delete.delete()
    return redirect('/notes/')

# View only a subcategory
def view_subcategory(request, category, subcategory):
    context = {
        'all_category_notes' : Note.objects.filter(category=subcategory),
        'all_notes' : Note.objects.filter(category=category),
        'category_name' : category,
        'subcategory_name' : subcategory,
        'list_of_categories' : Category.objects.all(),
        'list_of_subcategories' : Subcategory.objects.all(),
        'current_user' : User.objects.get(id=request.session['active_user']),
        'list_of_note_comments': NoteComment.objects.all(),
    }
    return render(request, "note_app/view_subcategory.html", context)

# def view_category_subcategory(request, category, subcategory):
#     context = {
#         'all_category_notes' : Note.objects.filter(category=subcategory),
#         'category_name' : category,
#         'subcategory_name' : subcategory,
#         'current_user' : User.objects.get(id=request.session['active_user'])
#     }
#     return render(request, "note_app/view_category_subcategory.html", context)
#     # return redirect('/notes/')

def add_note_from_category(request):
    print("Adding note from category")
    category = request.POST['category_name']
    subcategory = request.POST['subcategory_name']    
    Note.objects.create(title=request.POST['title'], category=request.POST['category'], content=request.POST['content'])
    return redirect('/notes/category/view/' + category + "/" + subcategory)

def add_note_comment_from_category(request, note_id):
    if request.method == 'POST':
        category = request.POST['category_name']
        subcategory = request.POST['subcategory_name']
        print(category)
        print(subcategory)
        print("Length:", len(request.FILES))
        if len(request.FILES) > 0:
            print("File provided!")
            parent = Note.objects.get(id=note_id)
            image = request.FILES['myfile']
            NoteComment.objects.create(content=request.POST['content'], parent=parent, isCode=request.POST['isCode'], image=image)
            return redirect('/notes/category/view/' + category + "/" + subcategory)
        else:
            print("No file provided!")
            parent = Note.objects.get(id=note_id)
            NoteComment.objects.create(content=request.POST['content'], parent=parent, isCode=request.POST['isCode'])
            return redirect('/notes/category/view/' + category + "/" + subcategory)
    return redirect('/notes/')

def master_list(request):
    context = {
        'all_notes' : Note.objects.all(),
        'current_user' : User.objects.get(id=request.session['active_user'])
    }
    return render(request, "note_app/master_list.html", context)