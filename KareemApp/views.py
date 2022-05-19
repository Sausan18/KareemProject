from django.shortcuts import render


def login(request):
    return render(request, 'login.html')


def registrasi(request):
    return render(request, 'registrasi.html')
