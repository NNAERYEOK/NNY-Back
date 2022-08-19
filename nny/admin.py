from django.contrib import admin
from .models import User, Train, Seat

# Register your models here.

admin.site.register(User)
admin.site.register(Train)

@admin.register(Seat)
class MyAdmin(admin.ModelAdmin):
    list_display = ['id', 'train', 'seat_num', 'is_seated', 'station']
    list_display_links = ['id', 'train', 'seat_num', 'is_seated', 'station']

    def short_content(self, seat):
        return seat.content[:10]