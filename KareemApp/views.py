from django.shortcuts import render


def login(request):
    return render(request, 'login.html')


def registrasi(request):
    return render(request, 'registrasi.html')

def amalanku(request):
    return render(request, 'amalanku.html')

def landingpage(request):
    return render(request, 'landingpage.html')

def dashboard(request):
    return render(request, 'dashboard.html')

def foodrekom(request):
    return render(request, 'foodrekom.html')
