from django import forms
from .models import Booking, RoomAvailability, Room 

class BookingForm(forms.ModelForm):
    check_in_date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    check_out_date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    
    class Meta:
        model = Booking 
        fields = ['room', 'check_in_date', 'check_out_date']

   

    def __init__(self, *args, **kwargs):
        room_id = kwargs.pop('room_id', None)  # Remove 'room_id' from kwargs
        super().__init__(*args, **kwargs)
# load room choices
        self.fields['room'].queryset = Room.objects.all()
        if room_id:
            self.initial['room'] = room_id  # Pre-populate the 'room' field if room_id is provided