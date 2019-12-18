from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'^$', views.index),
    url(r'^registration$', views.register_page),
    url(r'^register$', views.register),
    url(r'^login$', views.login),
    url(r'^login/guest$', views.login_as_guest),
    url(r'^dashboard$', views.dashboard),
    url(r'^logout$', views.logout),
]
