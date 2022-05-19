from django.db import models

# Create your models here.

class Users(models.Model):
    user_id = models.AutoField(primary_key=True)
    nama = models.CharField(max_length=500)
    username = models.CharField(max_length=500)
    password = models.CharField(max_length=500)


class Amalan(models.Model):
    amalan_id = models.AutoField(primary_key=True)
    nama_amalan = models.CharField(max_length=500)


class Aktivitas(models.Model):
    aktivitas_id = models.AutoField(primary_key=True)
    kode_jadwal = models.CharField(max_length=500)
    status = models.CharField(max_length=500)
    amalan = models.IntegerField()
    user = models.IntegerField()