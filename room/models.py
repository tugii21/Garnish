from django.db import models
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _

class Room(models.Model):
    ROOM_TYPES = (
        ('1', 'Single Room'),
        ('2', 'Double Room'),
        ('3', 'Ensuite Room'),
    )
    room_type = models.IntegerField(choices=ROOM_TYPES, default=1)
    # 
    def bookings(self):
        # Retrieve bookings associated with this room
        return Booking.objects.filter(room=self)
    def __str__(self):
        return f"{self.get_room_type_display()} Room"  # Corrected line
    #def __str__(self):
     #   return f"Booking for {self.room} by {self.user}"

class Booking(models.Model):
    ROOM_STATUS_CHOICES = (
        ('booked', 'Booked'),
        ('cancelled', 'Cancelled'),
    )
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    check_in_date = models.DateField()
    check_out_date = models.DateField()
    status = models.CharField(max_length=10, choices=ROOM_STATUS_CHOICES, default='booked')
    # 
    def __str__(self):
        return f"Booking for {self.room} by {self.user}"
class RoomAvailability(models.Model):
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    date = models.DateField()
    available = models.BooleanField(default=True)

    class Meta:
        unique_together = ('room', 'date')
        verbose_name_plural = 'Room Availabilities'

    def __str__(self):
        return f"{self.room} - {self.date} - {'Available' if self.available else 'Not Available'}"

    def clean(self):
        if self.available:
            if Booking.objects.filter(room=self.room, check_in_date=self.date).exists():
                raise ValidationError(_('This room is already booked for this date.'))

