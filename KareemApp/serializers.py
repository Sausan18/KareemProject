from rest_framework import serializers
from KareemApp.models import Users, Aktivitas


class UsersSerializers(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = ('user_id', 'nama', 'username', 'password')


class AktivitasSerializers(serializers.ModelSerializer):
    class Meta:
        model = Aktivitas
        fields = ('aktivitas_id', 'kode_jadwal', 'status', 'amalan', 'user')
