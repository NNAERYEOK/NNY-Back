from rest_framework import serializers
from .models import *
from django.contrib.auth import authenticate
from django.contrib.auth.password_validation import validate_password

class UserSerializer(serializers.ModelSerializer):
    profile='ProfileSerializer(many=False,read_only=True)'
    class Meta:
        model = User
        fields = ['pk','name','profile','username']
        extra_kwargs={
            "profile":{'read_only':True}
        }

class ProfileSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    class Meta:
        model = Profile
        fields = "__all__"

class UpdateProfileSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True,many=False)
    class Meta:
        model = Profile
        fields = "__all__"

    def get_profile(self,instance,data):
        instance.bio = data.get('eye', instance.eye)
        instance = super().get_fields(instance, data)
        return instance

    def update(request, instance, validated_data):
        instance.eye = validated_data['eye']

        instance.save()
        instance=super().update(instance,validated_data)
        return instance


class LoginSerializer(serializers.Serializer):
    name = serializers.CharField(write_only=True, required=True)
    password = serializers.CharField(write_only=True, required=True)
    
    def validate_user(self):
        new_user = authenticate(
            name=self.validated_data["name"],
            password=self.validated_data["password"],
        )
        if new_user is not None:
            return new_user
        raise serializers.ValidationError("The User does not Exist")

# User create serializer
class UserCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("id", "name", "username", "password")
        extra_kwargs = {"password": {"write_only": True}}

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user


# Changing the password
class ChangePasswordSerializer(serializers.ModelSerializer):
    
    password = serializers.CharField(write_only=True, required=True, validators=[validate_password])
    password2 = serializers.CharField(write_only=True, required=True)
    old_password = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = User
        fields = ('old_password', 'password', 'password2')

    def validate(self, attrs):
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError({"password": "Password fields didn't match."})

        return attrs

    def validate_old_password(self, value):
        user = self.context['request'].user
        if not user.check_password(value):
            raise serializers.ValidationError({"old_password": "Old password is not correct"})
        return value

            
    def update(self, instance, validated_data):
        user = self.context['request'].user

        if user.pk != instance.pk:
            raise serializers.ValidationError({"authorize": "You dont have permission for this user."})

        instance.set_password(validated_data['password'])
        instance.save()

        return instance
    
    
class WarningListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Warnings
        fields = '__all__'

class UsedEyeSerializer(serializers.ModelSerializer):
    class Meta:
        model = UsedEye
        fields = '__all__'

class EyeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Eye
        fields= '__all__'