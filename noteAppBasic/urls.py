from django.conf.urls import url, include
urlpatterns = [
    url(r'^', include('apps.note_app.urls')),
]
