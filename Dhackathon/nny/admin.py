from django.contrib import admin
from nny.models import CustomUser, Train, Seat

# Register your models here.

admin.site.register(CustomUser)
admin.site.register(Train)

@admin.register(Seat)
class MyAdmin(admin.ModelAdmin):
    list_display = ['id', 'train', 'seat_num', 'is_seated', 'station']
    list_display_links = ['id', 'train', 'seat_num', 'is_seated', 'station']

    def short_content(self, seat):
        return seat.content[:10]
