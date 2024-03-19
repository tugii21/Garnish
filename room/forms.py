from django import forms
from django.core.exceptions import ValidationError
from django.utils import timezone
from .models import Booking, Room

class BookingForm(forms.ModelForm):
    check_in_date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    check_out_date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    
    class Meta:
        model = Booking
        fields = ['room', 'check_in_date', 'check_out_date']

    def clean_check_in_date(self):
        check_in_date = self.cleaned_data.get('check_in_date')
        if check_in_date < timezone.now().date():
            raise forms.ValidationError("Check-in date cannot be in the past.")
        return check_in_date


    def __init__(self, *args, **kwargs):
        room_id = kwargs.pop('room_id', None)  # Remove 'room_id' from kwargs
        super().__init__(*args, **kwargs)
        # Load room choices
        self.fields['room'].queryset = Room.objects.all()
        if room_id:
            self.initial['room'] = room_id  # Pre-populate the 'room' field if room_id is provided

    def clean_check_out_date(self):
        check_out_date = self.cleaned_data.get('check_out_date')
        check_in_date = self.cleaned_data.get('check_in_date')

        if check_out_date <= timezone.now().date():
            raise ValidationError("Check-out date cannot be in the past.")

        if check_in_date and check_out_date <= check_in_date:
            raise ValidationError("Check-out date must be after the check-in date.")

        return check_out_date
