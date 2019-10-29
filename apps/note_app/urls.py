from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'^$', views.index),
    url(r'^note/add$', views.add_note),
    url(r'^note/edit/(?P<note_id>\d+)$', views.edit_note),
    url(r'^note/update$', views.update_note),
    url(r'^note/delete/(?P<note_id>\d+)$', views.delete_note),
    url(r'^note/move_up/(?P<note_id>\d+)$', views.move_up),
    url(r'^note/move_down/(?P<note_id>\d+)$', views.move_down),
]
