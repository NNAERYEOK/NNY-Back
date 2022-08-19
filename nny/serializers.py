from rest_framework import serializers
from .models import *
from django.contrib.auth import login
from rest_framework.response import Response
from django.contrib.auth.hashers import make_password
from rest_framework_simplejwt.tokens import RefreshToken

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'email', 'password', 'username']

    def create(self, validated_data):
        user = User.objects.create(
            email=validated_data['email'])
        user.set_password(validated_data['password'])
        user.save()
        login(self.context['request'], user)
        return user


class UserLoginSerializer(serializers.Serializer):
    email = serializers.EmailField(max_length=64)
    password = serializers.CharField(max_length=128, write_only=True)

    def validate(self, data):
        email = data.get("email", None)
        password = data.get("password", None)

        if User.objects.filter(email=email).exists():
            user = User.objects.get(email=email)
            if not user.check_password(password):
                raise serializers.ValidationError('잘못된 비밀번호')
            else:
                token = RefreshToken.for_user(user)
                refresh = str(token)
                access = str(token.access_token)

                data = {
                    'user': user.email,
                    'access_token': access,
                    'username': user.username
                }

                return data
        else:
            raise serializers.ValidationError('존재하지 않는 유저')

class Profileserialzier(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'password', 'eyes']

class PasswordChangeSerializer(serializers.Serializer):
    password = serializers.CharField(max_length=128, write_only=True)

    def update(self, instance : User, validated_data):
        instance.password = make_password(validated_data['password'])
        instance.save()
        return Response()

    def create(self, validated_data):
        pass

class SeatSerializer(serializers.ModelSerializer):
    class Meta:
        model = Seat
        fields = ['id', 'user', 'train', 'seat_num', 'is_seated', 'station']

class TrainSerializer(serializers.ModelSerializer):
    seat = SeatSerializer(many=True, read_only=True)

    class Meta:
        model = Train
        fields = ['id', 'train_id', 'seat']

class UsedEyeSerializer(serializers.ModelSerializer):
    class Meta:
        model = UsedEye
        fields = ['user', 'created_at', 'amount']

class EyeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Eye
        fields = ['user', 'created_at', 'amount']

class WarningSerializer(serializers.ModelSerializer):
    class Meta:
        model = Warning
        fields = ['user', 'created_at', 'station']