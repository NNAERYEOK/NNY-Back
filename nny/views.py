from django.shortcuts import get_object_or_404
from .serializers import *
from .models import *
from rest_framework import views
from rest_framework.response import Response
from rest_framework.status import *
from django.contrib.auth import login, logout

# Create your views here.

class SignUpView(views.APIView):
    def post(self, request, format=None):
        serializer = UserSerializer(
            context={'request': request}, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': '회원가입 성공', 'data': serializer.data})
        return Response({'message': '회원가입 실패', 'data': serializer.errors})

    def get(self, request):
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response({'message': '유저 목록 조회 성공', 'data': serializer.data}, status=HTTP_200_OK)

    def patch(self, request):
        uid = request.user.id
        user = User.objects.get(id=uid)
        if user is None:
            return Response({'message': '유저가 존재하지 않습니다.'}, status=HTTP_400_BAD_REQUEST)
        serializer = UserSerializer(user, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'username 입력 성공', 'data': serializer.data}, status=HTTP_200_OK)
        return Response({'message': 'username 입력 실패', 'data': serializer.errors}, status=HTTP_400_BAD_REQUEST)

class LoginView(views.APIView):
    def post(self, request):
        serializer = UserLoginSerializer(data=request.data, partial=True)
        if serializer.is_valid():
            user = serializer.validated_data
            login(request, user)
            return Response({'message': "로그인 성공", 'data': serializer.data}, status=HTTP_200_OK)
        return Response({'message': "로그인 실패", 'data': serializer.errors}, status=HTTP_400_BAD_REQUEST)

class LogoutView(views.APIView):
    def get(self, request, format=None):
        logout(request)
        return Response({'message': "로그아웃 성공"}, status=HTTP_200_OK)

class ProfileView(views.APIView):
    def get(self, request):
        uid = request.user.id
        user = User.objects.get(id=uid)
        serializer = Profileserialzier(user)
        return Response({'data': serializer.data}, status=HTTP_200_OK)
    
    def patch(self, request):
        uid = request.user.id
        user = User.objects.get(id=uid)
        serializer = Profileserialzier(user, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'eye 성공', 'data': serializer.data}, status=HTTP_200_OK)

class PasswordChangeView(views.APIView):
    serializer_class = PasswordChangeSerializer
    
    def post(self, request):
        uid = request.user.id
        user = User.objects.get(id=uid)
        user.set_password(request.data.get('password'))
        print(request.data.get('password'))
        print(request.data)
        user.save()
        return Response({'message': "비밀번호 변경 성공"}, status=HTTP_200_OK)

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

class SeatListView(views.APIView):
    def get(self, request, format=None):
        seats=Seat.objects.all()
        serializer=SeatSerializer(seats, many=True)
        return Response(serializer.data)

class SeatDetailView(views.APIView):
    def get(self, request, pk, format=None):
        seat = get_object_or_404(Seat, pk=pk)
        serializer = SeatSerializer(seat)
        return Response(serializer.data)

    def get_object(self, pk):
        return Seat.objects.get(pk=pk)

    def patch(self, request, *args, **kwargs):
        pk = self.kwargs.get('pk')
        seat_object = self.get_object(pk)
        serializer = SeatSerializer(seat_object, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'message':'좌석 정보 기입 성공', 'data':serializer.data})
        return Response({'message':'좌석 정보 기입 실패', 'error':serializer.errors})

class UsedEyeView(views.APIView):
    def patch(self, request):
        uid = request.user.id
        user = User.objects.get(id=uid)
        serializer = UsedEyeSerializer(user, data=request.data)
        if serializer.is_valid():
            serializer.save()  
            return Response({'message': 'Used Eye 생성 성공', 'data': serializer.data}, status=HTTP_200_OK)
        return Response({'message': 'Used Eye 생성 실패', 'data': serializer.errors}, status=HTTP_400_BAD_REQUEST)

    def get(self, request):
        usedeye = UsedEye.objects.all()
        serializer = UsedEyeSerializer(usedeye, many=True)
        return Response({'message': 'Used Eye 조회 성공', 'data': serializer.data}, status=HTTP_200_OK)

class EyeView(views.APIView):
    def patch(self, request):
        uid = request.user.id
        user = User.objects.get(id=uid)
        serializer = EyeSerializer(user, data=request.data)
        if serializer.is_valid():
            serializer.save()  
            return Response({'message': 'Eye 생성 성공', 'data': serializer.data}, status=HTTP_200_OK)
        return Response({'message': 'Eye 생성 실패', 'data': serializer.errors}, status=HTTP_400_BAD_REQUEST)

    def get(self, request):
        eye = Eye.objects.all()
        serializer = EyeSerializer(eye, many=True)
        return Response({'message': 'Eye 조회 성공', 'data': serializer.data}, status=HTTP_200_OK)

class WarningView(views.APIView):
    def patch(self, request):
        uid = request.user.id
        user = User.objects.get(id=uid)
        serializer = WarningSerializer(user, data=request.data)
        if serializer.is_valid():
            serializer.save() 
            return Response({'message': '경고 생성 성공', 'data': serializer.data}, status=HTTP_200_OK)
        return Response({'message': '경고 생성 실패', 'data': serializer.errors}, status=HTTP_400_BAD_REQUEST)

    def get(self, request):
        warning = Warning.objects.all()
        serializer = WarningSerializer(warning, many=True)
        return Response({'message': '경고 조회 성공', 'data': serializer.data}, status=HTTP_200_OK)
