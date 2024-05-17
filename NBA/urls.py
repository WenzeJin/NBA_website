from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('admin/', admin.site.urls),
    path('bbs/', include(('BBS.urls','BBS'), namespace='bbs')),
    path('', include(('Stats.urls', 'Stats'), namespace='stats')),
    path('ckeditor/', include('ckeditor_uploader.urls'), name='ckeditor'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
