from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class User(AbstractUser):
    name = models.CharField(max_length=255, unique=True, default = False)
    username = None

    USERNAME_FIELD = "name"
    REQUIRED_FIELDS = []

    def __str__(self):
        return f"{self.name}"

    def save_user(self):
        self.save()

    def delete_user(self):
        self.delete()


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    eye = models.IntegerField()
    

    def __str__(self):
        return f"{self.user.name}"

    def save_profile(self):
        self.save()

    def delete_profile(self):
        self.delete()

    @classmethod
    def update_profile(cls, user, eye):
        profile = cls.objects.filter(user=user).update(eye=eye)

        return profile




class Warnings(models.Model):
    user = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    station = models.IntegerField()
    
class UsedEye(models.Model):
    user = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add = True)
    amount = models.IntegerField()

class Eye(models.Model):
    user = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add = True)
    amount = models.IntegerField()