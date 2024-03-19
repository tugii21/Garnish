from django.contrib import admin
from .models import RoomAvailability ,Room, Booking

# Register your models here.
admin.site.register(RoomAvailability)
admin.site.register(Room)
admin.site.register(Booking)


