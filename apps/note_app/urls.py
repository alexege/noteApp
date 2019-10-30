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
    url(r'^note/edit_note_comment/(?P<note_comment_id>\d+)$', views.edit_note_comment)
]
