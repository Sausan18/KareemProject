from django.urls import re_path
from KareemApp import views

from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    re_path(r'^$', views.login, name='login'),
    re_path(r'^login', views.login, name='login'),
    re_path(r'^logout', views.logoutUser, name='logout'),
    re_path(r'^registrasi', views.registrasi),
    re_path(r'^amalanku', views.amalanku),
    re_path(r'^landingpage', views.landingpage),
    re_path(r'^dashboard', views.dashboard),
    re_path(r'^foodrekom', views.foodrekom),
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
