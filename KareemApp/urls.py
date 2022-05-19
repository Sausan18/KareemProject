from django.urls import re_path
from KareemApp import views

from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    re_path(r'^$', views.login, name='login'),
    re_path(r'^login', views.login, name='login'),
    re_path(r'^registrasi', views.registrasi),
    re_path(r'^amalanku', views.amalanku),
    re_path(r'^landingpage', views.landingpage),
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
