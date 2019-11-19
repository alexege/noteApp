from django.conf.urls import url
from . import views
urlpatterns = [
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
    url(r'^category/add$', views.add_category),
    
    url(r'^note/add_from_category$', views.add_note_from_category),
    url(r'^note/new_note_comment_from_category/(?P<note_id>\d+)$', views.add_note_comment_from_category),
    
    url(r'^category/note_comment/delete/(?P<note_comment_id>\d+)/(?P<category>[\w\s]+)/(?P<subcategory>[\w\s]+)$', views.delete_note_comment_from_category),
    url(r'^subcategory/add/(?P<category_id>\d+)$', views.add_subcategory),
    url(r'^subcategory/delete/(?P<subcategory_id>\d+)$', views.delete_subcategory),
    # url(r'^category/view/(?P<subcategory>[\w\s]+)$', views.view_subcategory),
    url(r'^category/view/(?P<category>[\w\s]+)/(?P<subcategory>[\w\s]+)$', views.view_subcategory),
    url(r'^category/view/all$', views.index),
    
    url(r'^master_list$', views.master_list),
    url(r'^toggle_note_privacy/(?P<subcat_id>\d+)$', views.privacyToggle),
]
