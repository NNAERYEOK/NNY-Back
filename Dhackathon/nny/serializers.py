from rest_framework import serializers
from .models import *

class SeatSerializer(serializers.ModelSerializer):
    class Meta:
        model = Seat
        fields = ['id', 'user', 'train', 'seat_num', 'is_seated', 'station']

class TrainSerializer(serializers.ModelSerializer):
    seat = SeatSerializer(many=True, read_only=True)

    class Meta:
        model = Train
        fields = ['id', 'train_id', 'seat']