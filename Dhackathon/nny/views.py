from django.shortcuts import render
from .models import *
from django.views.generic import ListView
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework.permissions import IsAuthenticated
from rest_framework import status, mixins, generics
from django.contrib.auth import authenticate, login, logout
from .serializers import *
from rest_framework.views import APIView
from drf_yasg.utils import swagger_auto_schema

class LoginAPIView(APIView):
    @swagger_auto_schema(request_body=LoginSerializer)
    def post(self, request, format=None):
        serializer = LoginSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.validate_user()
            data = {
                "message": "User logged in successfully",
                "name": user.name,
                "user_id":user.id
            }

            # get auth token
            token, created = Token.objects.get_or_create(user=user)
            data["token"] = token.key
            # data["User"]=user

            responseStatus = status.HTTP_200_OK

            return Response(data, status=responseStatus)

        else:
            Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class UserCreateAPIView(APIView):
    @swagger_auto_schema(request_body=UserCreateSerializer)
    def post(self, request, format=None):
        data = request.data
        print("data",data)
        name = data["name"]

        serializer = UserCreateSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user_type=user_type)
            data = {"name": data["name"], "message": "User created successfully"}

            return Response(data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class LogoutAPIView(APIView):
    def get(self, request, format=None):
        logout(request)
        return Response(status=status.HTTP_200_OK)


class ChangePasswordView(generics.UpdateAPIView):

    queryset = User.objects.all()
    permission_classes = (IsAuthenticated,)
    serializer_class = ChangePasswordSerializer
    
class ProfileAPIview(generics.GenericAPIView):
    lookup_field = 'user'
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer

    def get(self, request, pk=None):
        instance = self.get_object()
        print("instance",instance)
        instance.eye=request.data['eye']
        instance.get_fields=['eye']
        return Response('done')



class ProfileUpdateAPIview(generics.GenericAPIView):
    lookup_field = 'user'
    queryset = Profile.objects.all()
    serializer_class = UpdateProfileSerializer

    def put(self, request, pk=None):
        instance = self.get_object()
        print("instance",instance)
        instance.eye=request.data['eye']
        instance.save(update_fields=['eye'])
        return Response('done')    
    


class WarningListView(generics.GenericAPIView, mixins.ListModelMixin):
    serializer_class = WarningListSerializer
    def get_queryset(self):
        return Warnings.objects.all().order_by('id')
    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

class WarningView(ListView):
    def get_queryset(self, **kwargs):
        queryset = Warnings.objects.filter(id = self.request.session.get('user'))
        return queryset

class UsedEyeListView(generics.GenericAPIView, mixins.ListModelMixin):
    serializer_class = UsedEyeSerializer
    def get_queryset(self):
        return UsedEye.objects.all().order_by('id')
    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

class UsedEyeView(ListView):
    def get_queryset(self, **kwargs):
        queryset = UsedEye.objects.filter(id = self.request.session.get('user'))
        return queryset

class EyeListView(generics.GenericAPIView, mixins.ListModelMixin):
    serializer_class = EyeSerializer
    def get_queryset(self):
        return Eye.objects.all().order_by('id')
    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

class EyeView(ListView):
    def get_queryset(self, **kwargs):
        queryset = Eye.objects.filter(id = self.request.session.get('user'))
        return queryset
    
    
    