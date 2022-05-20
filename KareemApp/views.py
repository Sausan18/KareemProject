from django.shortcuts import render

from django.shortcuts import redirect, render
from django.contrib import messages
from django.contrib.auth import logout


from KareemApp.models import Users, Aktivitas
from KareemApp.serializers import UsersSerializers, AktivitasSerializers


def login(request):
    if request.method == 'GET':
        return render(request, 'login.html')
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        try:
            user = Users.objects.get(
                username=username, password=password)
        except Users.DoesNotExist:
            messages.error(request, 'Pengguna tidak ditemukan!')
            return redirect('/login')

        request.session['user_id'] = user.user_id
        return redirect('/dashboard')


def registrasi(request):
    if request.method == 'GET':
        return render(request, 'registrasi.html')
    elif request.method == 'POST':
        user_data = {
            'nama': request.POST['nama'],
            'username': request.POST['username'],
            'password': request.POST['password'],
        }

        password = request.POST['password']
        konfirmasi_password = request.POST['konfirpass']

        if password != konfirmasi_password:
            messages.error(request, "Konfirmasi password tidak cocok!")
            return redirect('/registrasi')

        try:
            user = Users.objects.get(username=user_data['username'])
            messages.error(request, "Pengguna sudah ada!")
            return redirect('/registrasi')
        except:
            pass

        user_serializer = UsersSerializers(data=user_data)

        if user_serializer.is_valid():
            user_serializer.save()
            messages.success(request, "Pendaftaran berhasil!")
            return redirect('/login')

        messages.error(request, 'Gagal menambahkan pemberi baru!')
        return redirect('/login')


def amalanku(request):
    return render(request, 'amalanku.html')


def landingpage(request):
    return render(request, 'landingpage.html')


def dashboard(request):
    return render(request, 'dashboard.html')


def foodrekom(request):
    return render(request, 'foodrekom.html')


def logout(request):
    logout(request)
    return redirect('/login')
