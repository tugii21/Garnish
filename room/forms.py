from django import forms
from django.core.exceptions import ValidationError
from django.utils import timezone
from .models import Booking

class BookingForm(forms.ModelForm):
    check_in_date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    check_out_date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    
    class Meta:
        model = Booking
        fields = ['room', 'check_in_date', 'check_out_date']

    def clean(self):
        cleaned_data = super().clean()
        check_in_date = cleaned_data.get('check_in_date')
        check_out_date = cleaned_data.get('check_out_date')
        room = cleaned_data.get('room')

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

        # Check if dates are in the past
        if check_in_date < timezone.now().date():
            raise ValidationError("Check-in date cannot be in the past.")

        if check_out_date < timezone.now().date():
            raise ValidationError("Check-out date cannot be in the past.")
