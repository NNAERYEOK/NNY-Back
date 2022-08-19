from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.

class CustomUserManager(BaseUserManager):
    def create_user(self, email, password, **extra_fields):
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(email=self.normalize_email(email), **extra_fields)
        user.set_password(password)
        user.save()
        return user
    
    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self.create_user(email=self.normalize_email(email), password=password, **extra_fields)

class User(AbstractUser):
    email = models.EmailField(max_length=20, unique=True)
    username = models.CharField(max_length=40, unique=False, default='')
    eyes = models.CharField(max_length=40, default='')
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    objects = CustomUserManager()

class Profile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    

class Train(models.Model):
    train_id = models.IntegerField()

class Seat(models.Model):
    train = models.ForeignKey(Train, on_delete=models.CASCADE, related_name='seat')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    seat_num = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(36)])
    is_seated = models.BooleanField(default=False)
    station = models.IntegerField(null=True, blank=True, validators=[MinValueValidator(1), MaxValueValidator(63)])

class UsedEye(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, related_name='usedeye')
    created_at = models.DateTimeField(null = True, blank = True)
    amount = models.IntegerField()

class Eye(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, related_name='eye')
    created_at = models.DateTimeField(null = True, blank = True)
    amount = models.IntegerField()

class Warning(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, related_name='warning')
    created_at = models.DateTimeField(null = True, blank = True)
    station = models.IntegerField(null=True, blank=True, validators=[MinValueValidator(1), MaxValueValidator(63)])