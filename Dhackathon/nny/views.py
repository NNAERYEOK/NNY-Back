from django.shortcuts import get_object_or_404
from .serializers import *
from .models import *
from rest_framework import views
from rest_framework.response import Response

# Create your views here.

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
        return Response(serializer.data)