from django import forms
from django.core.exceptions import ValidationError
from django.utils import timezone
from .models import Booking
from django.utils.translation import gettext_lazy as _


class BookingForm(forms.ModelForm):
    # Define form fields with appropriate widgets
    check_in_date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    check_out_date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    
    class Meta:
        # Specify the model and fields to be included in the form
        model = Booking
        fields = ['room', 'check_in_date', 'check_out_date']

    def clean(self):
        """
        Clean and validate form data before saving.

        This method performs validation on the form's cleaned data. It checks if the room, check-in date,
        and check-out date are provided. It also validates that the check-in date is not in the past, the
        check-out date is after the check-in date, and that there are no conflicts with existing bookings.

        Raises:
        ValidationError: If room, check-in date, or check-out date is not provided.
                     If check-in date is in the past.
                     If check-out date is in the past.
                     If the room is already booked for the provided date.
                     If the selected dates conflict with existing bookings.
                     If check-out date is not after the check-in date.
         """ 
        cleaned_data = super().clean()
        check_in_date = cleaned_data.get('check_in_date')
        check_out_date = cleaned_data.get('check_out_date')
        room = cleaned_data.get('room')

        # Check if either room or date is None
        if room is None or check_in_date is None or check_out_date is None:
            raise ValidationError(_('Room and date must be provided.'))

        # Check if dates are in the past
        if check_in_date < timezone.now().date():
            raise ValidationError("Check-in date cannot be in the past.")

        # Check if check-out date is after check-in date
        if check_out_date < timezone.now().date():
            raise ValidationError("Check-out date cannot be in the past.")

        # Existing validation logic
        if Booking.objects.filter(room=room, check_in_date=check_in_date).exists():
            raise ValidationError(_('This room is already booked for this date.'))

        # Check for conflicts with existing bookings
        conflicting_bookings = Booking.objects.filter(
            room=room,
            check_in_date__lt=check_out_date,
            check_out_date__gt=check_in_date,
        ).exclude(id=self.instance.id if self.instance else None)

        if conflicting_bookings.exists():
            raise ValidationError("These dates are fully booked. Please select different dates")

        # Check if check-out date is after check-in date
        if check_out_date <= check_in_date:
            raise ValidationError("Check-out date must be after the check-in date.")
