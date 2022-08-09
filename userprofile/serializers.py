from attr import field
from rest_framework import serializers
from django.contrib.auth import get_user_model

from userprofile.models import UserData

class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = "__all__"

    def create(self, validated_data):
        return get_user_model().objects.create_user(**validated_data)

class UserDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserData
        fields = '__all__'