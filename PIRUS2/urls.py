from django.conf import settings
from django.views.static import serve 
from django.contrib import admin
from . import views
from django.urls import path, re_path, include

urlpatterns = [
    path('', views.Index.as_view()),
    path('about/', views.About.as_view()),
    path('admin/', admin.site.urls),
    path('', include('rumahsakit.urls')),
    path('', include('akun.urls')),
    path('', include('dokter.urls')),
    re_path(r'^media/(?P<path>.*)$', serve,{'document_root': settings.MEDIA_ROOT}),
]