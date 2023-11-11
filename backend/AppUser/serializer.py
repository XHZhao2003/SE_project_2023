from rest_framework import serializers
from AppUser.models import AppUser

class AppUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = AppUser
        fields = [
            'id',
            'username',
            'password',
        ]