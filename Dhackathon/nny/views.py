from django.shortcuts import render
import re
from django.contrib.auth import get_user_model, logout
from django.http import JsonResponse, HttpResponse
from drf_yasg.utils import swagger_auto_schema
from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from django.views.decorators.csrf import csrf_exempt
from rest_framework.pagination import PageNumberPagination
from .models import *
from . import serializers
from .serializers import *
from .utils import get_and_authenticate_user, create_user_account
from django.utils import timezone
from drf_yasg import openapi
from datetime import datetime, timedelta
from django.shortcuts import get_object_or_404
from .serializers import *
from .models import *
from rest_framework import views
from rest_framework.response import Response



User = get_user_model()

class TrainListView(views.APIView):
    def get(self, request, format=None):
        trains=Train.objects.all()
        serializer=TrainSerializer(trains, many=True)
        return Response(serializer.data)

class TrainDetailView(views.APIView):
    def get(self, request, pk, format=None):
        train = get_object_or_404(Train, pk=pk)
        serializer = TrainSerializer(train)
        return Response(serializer.data)

class SeatView(views.APIView):
    def patch(self, request, format=None):
        serializer = SeatSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

    def get(self, request, format=None):
        seats=Seat.objects.all()
        serializer=SeatSerializer(seats, many=True)
        point_action = Point_action.objects.get(action='착석')
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = get_and_authenticate_user(**serializer.validated_data)
        data = serializers.LoginSerializer(user).data
        uid = CustomUser.objects.get(id=data['id'])
        try:
            total_point = Point_List.objects.filter(uid=data['id']).order_by('-id')[0].total_point
            Point_List.objects.create(point=point_action.point_value,
                                            total_point=total_point + point_action.point_value,
                                            date=timezone.now(),
                                            action_id=point_action,
                                            detail_action='착석',
                                            uid=uid)
        except:
            Point_List.objects.create(point=point_action.point_value,
                                            total_point=point_action.point_value,
                                            date=timezone.now(),
                                            action_id=point_action,
                                            detail_action='착석',
                                            uid=uid)
            return Response(data = data, status=status.HTTP_200_OK)
        return Response(serializer.data)

class AuthViewSet(viewsets.GenericViewSet):
    permission_classes = [AllowAny, ]
    serializer_class = EmptySerializer
    serializer_classes = {
        'login': UserLoginSerializer,
        'register': UserRegisterSerializer,
        'password_change': PasswordChangeSerializer,
        'withdrawal': WithdrawalSerializer,
    }

    @csrf_exempt
    @action(methods=['POST', ], detail=False)
    def login(self, request):
        """ USER 로그인 --- User 로그인 : email과 password를 전송하면 토큰 발행 """
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = get_and_authenticate_user(**serializer.validated_data)
        data = serializers.LoginSerializer(user).data
        if data['withdrawal_status']:
            data = {"There is no member information."}
            return Response(data=data, status=status.HTTP_400_BAD_REQUEST)
        else:
            data = serializers.LoginSerializer(user).data

        return Response(data=data, status=status.HTTP_200_OK)

    @csrf_exempt
    @action(methods=['POST', ], detail=False)
    def register(self, request):
        """ USER 등록 --- 새로운 User 회원가입 : 개인정보 입력 후 가입 가능"""
        regex1 = re.compile(r'(?=.*[0-9])(?=.*[^\w\s]).*')
        regex2 = re.compile(r'(?=.*[0-9]).*')
        regex3 = re.compile(r'(?=.*[^\w\s]).*')

        if regex1.match(request.data['username']) is not None or regex2.match(request.data['username']) is not None or \
                regex3.match(request.data['username']) is not None:
            return Response(data={'username': ["이름에는 숫자나 특수문자를 포함할 수 없습니다."]}, status=status.HTTP_400_BAD_REQUEST)

        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = create_user_account(**serializer.validated_data)
        data = serializers.AuthUserSerializer(user).data

        return Response(data=data, status=status.HTTP_200_OK)

    @csrf_exempt
    @action(methods=['POST', ], detail=False)
    def logout(self, request):
        """ USER 로그아웃 """
        logout(request)
        data = {'success': 'Sucessfully logged out'}
        return Response(data=data, status=status.HTTP_200_OK)

    @csrf_exempt
    @action(methods=['POST'], detail=False, permission_classes=[IsAuthenticated, ])
    def password_change(self, request):
        """ USER 비민번호 변경 --- 기존 비밀번호와 변경할 비밀번호를 입력 후 비밀번호 변경 [token required]"""
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        request.user.set_password(serializer.validated_data['new_password'])
        request.user.save()
        data = {"Password change successful!"}
        return Response(data=data, status=status.HTTP_200_OK)

    @csrf_exempt
    @action(methods=['POST', ], detail=False)
    def user_info(self, request):
        """ USER 정보 리스트 출력 --- uid 번호와 USER email 정보 전송"""
        query_set = User.objects.all()
        serializer = UserInfoSerializer(query_set, many=True)
        return JsonResponse(serializer.data, safe=False)
        return Response(status=status.HTTP_200_OK)

    @swagger_auto_schema(request_body=openapi.Schema(
        type=openapi.TYPE_OBJECT,
        properties={
            'page_size': openapi.Schema(type=openapi.TYPE_INTEGER, description='한 페이지에 표시할 내역 수'),
            'start': openapi.Schema(type=openapi.TYPE_INTEGER, description='내역 시작 날짜'),
            'end': openapi.Schema(type=openapi.TYPE_INTEGER, description='내역 끝 날짜'),

        }))
    
    @csrf_exempt
    @action(methods=['POST', ], detail=False, permission_classes=[IsAuthenticated, ])
    def my_point_list(self, request):
        """ USER 포인트 내역 출력 [token required]"""
        start = datetime.strptime(request.data['start'], "%Y-%m-%d")
        end = datetime.strptime(request.data['end'], "%Y-%m-%d")

        paginator = PageNumberPagination()
        paginator.page_size = request.data['page_size']
        query_set = Point_List.objects.filter(uid=request.user.id,
                                                date__range=[start, end + timedelta(days=1)]).order_by("-id")

        result_page = paginator.paginate_queryset(query_set, request)
        serializer = PointListSerializer(result_page, many=True)
        return paginator.get_paginated_response(serializer.data)
        return Response(status=status.HTTP_200_OK)

    @csrf_exempt
    @action(methods=['GET', ], detail=False, permission_classes=[IsAuthenticated, ])
    def my_point(self, request):
        """ USER 현재 포인트 [token required]"""
        query_set = Point_List.objects.filter(uid=request.user.id).order_by("-id").first()
        serializer = PointSerializer(query_set)
        return JsonResponse(serializer.data, safe=False)
        return Response(status=status.HTTP_200_OK)
    
