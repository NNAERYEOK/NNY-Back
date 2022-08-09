from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.

class User(AbstractUser):
    email = models.EmailField(max_length=100, unique=True)

class Train(models.Model):
    train_id = models.IntegerField()

class Seat(models.Model):
    train = models.ForeignKey(Train, on_delete=models.CASCADE, related_name='seat')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    seat_num = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(36)])
    is_seated = models.BooleanField(default=False)
    station = models.IntegerField(null=True, blank=True, validators=[MinValueValidator(1), MaxValueValidator(63)])