from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.

class CustomUser(AbstractUser):
    username = models.CharField(max_length=50, default="")
    email = models.EmailField(unique=True)

    first_name = None
    last_name = None

    withdrawal_status = models.BooleanField(default=False)
    withdrawal_date = models.DateTimeField(blank=True, null=True)

    code = models.CharField(max_length=16, null=True, blank=True)

    forget_pwd_token = models.CharField(max_length=16, null=True, blank=True, default=None)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    def __str__(self):
        return f"{self.email} - {self.username}"

    class Meta:
        db_table = 'user'


class Register(models.Model):
    id = models.AutoField(primary_key=True)
    uid = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    username = models.CharField(max_length=500, blank=False, null=False)
    user_password = models.CharField(max_length=500, blank=False, null=False)

    class Meta:
        db_table = 'register'
        unique_together = ['uid']



class Point_action(models.Model):
    id = models.IntegerField(primary_key=True, unique=True)
    action = models.CharField(max_length=50)
    point_value = models.IntegerField()
    limit_number_of_day = models.SmallIntegerField()

    class Meta:
        db_table = 'point_action'


class Point_List(models.Model):
    id = models.AutoField(primary_key=True)
    action_id = models.ForeignKey(Point_action, on_delete=models.CASCADE)
    uid = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    point = models.IntegerField()
    total_point = models.IntegerField(default=0)
    date = models.DateTimeField()
    detail_action = models.CharField(max_length=50)

    class Meta:
        db_table = 'point_list'

class Train(models.Model):
    train_id = models.IntegerField()

class Seat(models.Model):
    train = models.ForeignKey(Train, on_delete=models.CASCADE, related_name='seat')
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    seat_num = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(36)])
    is_seated = models.BooleanField(default=False)
    station = models.IntegerField(null=True, blank=True, validators=[MinValueValidator(1), MaxValueValidator(63)])