from django import forms
from .models import Booking, Room

class BookingForm(forms.ModelForm):
    check_in_date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    check_out_date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))

    class Meta:
        model = Booking
        fields = ['room', 'check_in_date', 'check_out_date']

    def __init__(self, *args, **kwargs):
        room_id = kwargs.pop('room_id', None)
        super().__init__(*args, **kwargs)
        if room_id:
            self.fields['room'].initial = room_id  # Set the initial value for the 'room' field

    def clean(self):
        cleaned_data = super().clean()
        room_id = cleaned_data.get('room')
        if room_id:
            # Room ID is found, you can handle it here if needed
            pass