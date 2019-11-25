from django.conf.urls import url
from . import views
urlpatterns = [
    # Routes to homepage
    url(r'^$', views.index),
    url(r'^note/add$', views.add_note),
    url(r'^note/edit/(?P<note_id>\d+)$', views.edit_note),
    url(r'^note/update/(?P<note_id>\d+)$', views.update_note),
    url(r'^note/delete/(?P<note_id>\d+)$', views.delete_note),
    url(r'^note/move_up/(?P<note_id>\d+)$', views.move_up),
    url(r'^note/move_down/(?P<note_id>\d+)$', views.move_down),
    url(r'^note/new_note_comment/(?P<note_id>\d+)$', views.add_note_comment),
    url(r'^note/edit_note_comment/(?P<note_comment_id>\d+)$', views.edit_note_comment),
    url(r'^note_comment/delete/(?P<note_comment_id>\d+)$', views.delete_note_comment),
    
    url(r'^category/add$', views.add_notebook),   
    url(r'^subcategory/add/(?P<category_id>\d+)$', views.add_subcategory),
    
    # Routes from Category page
    url(r'^subcategory/delete/(?P<subcategory_id>\d+)$', views.delete_subcategory),
    url(r'^category/view/(?P<category>[\w\s]+)$', views.view_category),
    url(r'^category/view/All$', views.index),

    
    url(r'^master_list$', views.master_list),
    # url(r'^toggle_note_privacy/(?P<subcat_id>\d+)$', views.privacyToggle),
    url(r'^toggle_notebook_privacy/(?P<category_id>\d+)$', views.privacyToggle),
    url(r'^toggle_notebook_privacy_from_category/(?P<category_id>\d+)$', views.categoryPrivacyToggle),
    url(r'^category/delete/(?P<category_id>\d+)$', views.delete_category),

    url(r'^ajax/drag_and_drop/(?P<starting_note_id>\d+)/(?P<ending_note_id>\d+)$', views.drag_and_drop),
    url(r'^ajax/all_notes_partial$', views.all_notes_partial),

    url(r'^(?P<category>[\w\s]+)$', views.category)
]
