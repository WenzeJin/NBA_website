from django.contrib import admin
from django.contrib.auth.decorators import login_required
from django.urls import path, include, re_path
from django.conf.urls.static import static
from django.conf import settings
from django.views.decorators.cache import never_cache
from ckeditor_uploader import views as ckeditor_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('bbs/', include(('BBS.urls','BBS'), namespace='bbs')),
    path('', include(('Stats.urls', 'Stats'), namespace='stats')),
    #path('ckeditor/', include('ckeditor_uploader.urls'), name='ckeditor'),
    re_path(r'^ckeditor/upload/', login_required(ckeditor_views.upload), name='ckeditor_upload'),
    re_path(r'^ckeditor/browse/', never_cache(login_required(ckeditor_views.browse)), name='ckeditor_browse'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
