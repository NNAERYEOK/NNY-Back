from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class User(AbstractUser):
    email = models.EmailField(max_length=100, unique=True)

class Train(models.Model):
    train_id = models.IntegerField()

class Seat(models.Model):
    train = models.ForeignKey(Train, on_delete=models.CASCADE, related_name='seat')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    seat_num = models.IntegerField()
    is_seated = models.BooleanField(default=False)
    station = models.IntegerField()