from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('bbs/', include(('BBS.urls','BBS'), namespace='bbs')),
    path('', include(('Stats.urls', 'Stats'), namespace='stats')),
]
