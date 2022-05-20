from django.shortcuts import render

from django.shortcuts import redirect, render
from django.contrib import messages
from django.contrib.auth import logout


from KareemApp.models import Users, Aktivitas
from KareemApp.serializers import UsersSerializers, AktivitasSerializers


def login(request):
    return render(request, 'login.html')


def registrasi(request):
    if request.method == 'GET':
        return render(request, 'registrasi.html')
    # elif request.method == 'POST':
    #     return


def amalanku(request):
    return render(request, 'amalanku.html')


def landingpage(request):
    return render(request, 'landingpage.html')


def dashboard(request):
    return render(request, 'dashboard.html')
