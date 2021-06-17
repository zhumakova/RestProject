from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from .models import *

class ProfileSerializer(serializers.ModelSerializer):

    class Meta:
        model=Profile
        fields=['full_name']

class RegisterSerializer(serializers.ModelSerializer):
    check_password = serializers.CharField(min_length=6, write_only=True)
    profile = ProfileSerializer()

    class Meta:
        model = User
        fields = ['username', 'password', 'check_password', 'profile']

    def create(self, validated_data):
        password = validated_data.get('password')
        check_password = validated_data.pop('check_password')
        profile_data = validated_data.pop('profile')
        if password == check_password:
            user = User.objects.create_user(**validated_data)
            Profile.objects.create(user=user, **profile_data)
            return user
        raise ValidationError("Passwords don't match. Try again!")