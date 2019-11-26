from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'^$', views.index),
    url(r'^master_list$', views.master_list),

    #Notes
    url(r'^note/add$', views.add_note),
    url(r'^note/edit/(?P<note_id>\d+)$', views.edit_note),
    url(r'^note/delete/(?P<note_id>\d+)$', views.delete_note),
    
    #Comments
    url(r'^comment/add/(?P<note_id>\d+)$', views.add_comment),
    url(r'^comment/edit/(?P<note_comment_id>\d+)$', views.edit_comment),
    url(r'^comment/delete/(?P<note_comment_id>\d+)$', views.delete_comment),
    
    #Notebook
    url(r'^notebook/add$', views.add_notebook),
    # url(r'^notebook/view/(?P<category>[\w\s]+)$', views.view_notebook),
    url(r'^notebook/view/All$', views.index),
    url(r'^notebook/delete/(?P<category_id>\d+)$', views.delete_category),
    url(r'^notebook/(?P<notebook_id>\d+)/privacy$', views.togglePrivacy),

    #Category
    url(r'^subcategory/add/(?P<category_id>\d+)$', views.add_subcategory),
    url(r'^subcategory/delete/(?P<subcategory_id>\d+)$', views.delete_subcategory),

    #Ajax
    url(r'^ajax/drag_and_drop/(?P<starting_note_id>\d+)/(?P<ending_note_id>\d+)$', views.drag_and_drop),
    # url(r'^ajax/all_notes_partial$', views.all_notes_partial),
    url(r'^(?P<category>[\w\s]+)$', views.notebook_partial),
]
