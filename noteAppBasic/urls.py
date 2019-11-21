from django.conf.urls import url, include
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    url(r'^login/', include('apps.login_app.urls')),
    url(r'^notes/', include('apps.note_app.urls')),
    url(r'^', include('apps.login_app.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)