from django.contrib import admin
from .models import User, Train, Seat

# Register your models here.

admin.site.register(User)
admin.site.register(Train)
admin.site.register(Seat)