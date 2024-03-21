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
    room_type = models.CharField(max_length=2, choices=ROOM_TYPES, default='1')  # Changed to CharField
    bed = models.IntegerField()  # Field for bed type
    capacity = models.IntegerField()  # Field for capacity
    number = models.IntegerField()

    # 
    def __str__(self):
        return f"{self.room_type}"
    #def bookings(self):
     #   return Booking.objects.filter(room=self)
    #def __str__(self):
     #   return f"{self.get_room_type_display()} Room"  # Corrected line
    
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
    created_on = models.DateTimeField(auto_now_add=True)  # Automatically set the current date and time when an object is created

    # 
    def __str__(self):
        return f"{self.user} booked for  Room number {self.room} from {self.check_in_date} to {self.check_out_date} "
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
        if self.room is not None and self.date is not None:
            if self.available:
                if Booking.objects.filter(room=self.room, check_in_date=self.date).exists():
                    raise ValidationError(_('This room is already booked for this date.'))
        else:
            raise ValidationError(_('Room and date must be provided.'))

