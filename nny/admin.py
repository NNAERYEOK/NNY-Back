from django.contrib import admin
from .models import User, Train, Seat


admin.site.register(User) 
admin.site.register(Train)

class UserAdmin(admin.ModelAdmin):
    list_display = ['id', 'username', 'email', 'password']
    list_display_links = ['id', 'username']

@admin.register(Seat)
class MyAdmin(admin.ModelAdmin):
    list_display = ['id', 'train', 'seat_num', 'is_seated', 'station']
    list_display_links = ['id', 'train', 'seat_num', 'is_seated', 'station']

    def short_content(self, seat):
        return seat.content[:10]