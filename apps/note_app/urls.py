from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'^$', views.index),
    url(r'^master_list$', views.master_list),

    #Notebook
    url(r'^notebook/add$', views.add_notebook),
    url(r'^notebook/view/All$', views.index),
    url(r'^notebook/delete/(?P<notebook_id>\d+)$', views.delete_notebook),
    url(r'^notebook/edit/(?P<notebook_id>\d+)$', views.edit_notebook),
    url(r'^notebook/(?P<notebook_id>\d+)/privacy$', views.togglePrivacy),

    #Category
    url(r'^category/add/(?P<category_id>\d+)$', views.add_category),
    url(r'^category/delete/(?P<category_id>\d+)$', views.delete_category),

    #Notes
    url(r'^note/add/(?P<notebook_name>[\w\s]+)$', views.add_note),
    url(r'^note/edit/(?P<note_id>\d+)$', views.edit_note),
    url(r'^note/delete/(?P<note_id>\d+)$', views.delete_note),
    
    #Comments
    url(r'^comment/add/(?P<note_id>\d+)$', views.add_comment),
    url(r'^comment/edit/(?P<comment_id>\d+)$', views.edit_comment),
    url(r'^comment/delete/(?P<note_comment_id>\d+)$', views.delete_comment),
    url(r'^comment/toggleBullet/(?P<comment_id>\d+)/(?P<bullet_style>[\w\s]+)$', views.toggle_comment_bullet),

    #Ajax
    url(r'^ajax/drag_and_drop/(?P<starting_note_id>\d+)/(?P<ending_note_id>\d+)$', views.drag_and_drop),
    url(r'^ajax/drag_and_drop_notebooks/(?P<starting_notebook_id>\d+)/(?P<ending_notebook_id>\d+)$', views.drag_and_drop_notebook),
    # url(r'^(?P<notebook>[\w\s]+)/(?P<category>[\w\s]+)$', views.note_partial),
    url(r'^selected_notes/(?P<notebook>[\w\s]+)/(?P<category>[\w\s]+)$', views.note_partial),
    # url(r'^sidenav$', views.view_sidenav),
    url(r'^view/(?P<notebook_name>[\w\s]+)$', views.all_notebook_categories),
    # url(r'^public/(?P<category>[\w\s]+)$', views.public_note_partial),
    url(r'^all_notes/', views.all_my_notes),
    url(r'^comment/(?P<comment_id>\d+)/indent$', views.indent_comment),
    url(r'^comment/(?P<comment_id>\d+)/outdent$', views.outdent_comment),
]
