from rest_framework import serializers
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password

from .models import Picture


class PictureSerializer(serializers.ModelSerializer):
    class Meta:
        model = Picture
        fields = '__all__'
        read_only_fields = ['owner']
    
    def create(self, validated_data):
        validated_data.update({'owner':self.context['request'].user})
        return super().create(validated_data)
    

class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()


class RegisterAccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password']

    def create(self, validated_data):
        password = make_password(validated_data.get('password'))
        validated_data['password'] = password
        return super().create(validated_data)
    
    
class DetailUserSerializer(serializers.ModelSerializer):
     class Meta:
        model = User
        exclude = ['password', 'groups', 'user_permissions']
        read_only_fields = [
            "id",
            "is_superuser",
            "last_login",
            "is_staff",
            "is_active",
            "date_joined",
        ]