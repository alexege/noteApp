from django.conf.urls import url, include
urlpatterns = [
    url(r'^', include('apps.login_app.urls')),
    url(r'^login/', include('apps.login_app.urls')),
    url(r'^notes/', include('apps.note_app.urls')),
]
