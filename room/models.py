from django.db import models
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _

class Room(models.Model):
    # Choices for room types
    ROOM_TYPES = (
        ('1', 'Single Room'),
        ('2', 'Double Room'),
        ('3', 'Ensuite Room'),
    )
    room_type = models.CharField(max_length=2, choices=ROOM_TYPES, default='1')  # Changed to CharField
    bed = models.IntegerField()  # Field for bed type
    capacity = models.IntegerField()  # Field for capacity
    number = models.IntegerField()

    # String representation of the room
    def __str__(self):
        return f"{self.room_type}"

class Booking(models.Model):
    # Choices for room status
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

    # String representation of the booking
    def __str__(self):
        return f"{self.user} booked for  Room number {self.room} from {self.check_in_date} to {self.check_out_date} "
# Room for which availability is being tracked
class RoomAvailability(models.Model):
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    date = models.DateField()
    available = models.BooleanField(default=True)

    class Meta:
        # Ensure each room availability entry is unique based on room and data
        unique_together = ('room', 'date')
        verbose_name_plural = 'Room Availabilities'

    # String representation of the booking
    def __str__(self):
        """
         Return a string representation of the RoomAvailability object.

        Returns:
         str: A string containing the room name, date, and availability status.
        """
        return f"{self.room} - {self.date} - {'Available' if self.available else 'Not Available'}"

    # Validate room availability
    def clean(self):
        """
        Clean and validate room availability before saving.

        This method checks if the room and date are provided. If the room is available, it validates
        that the room is not already booked for the provided date.

        Raises:
        ValidationError: If room or date is not provided.
                     If the room is already booked for the provided date.
        """
        if self.room is not None and self.date is not None:
            if self.available:
                # Check if the room is already booked for this date
                if Booking.objects.filter(room=self.room, check_in_date=self.date).exists():
                    raise ValidationError(_('This room is already booked for this date.'))
        else:
            # Raise validation error if room or date is not provided
            raise ValidationError(_('Room and date must be provided.'))

