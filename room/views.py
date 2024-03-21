from django.shortcuts import render, redirect, get_object_or_404
from .models import Room, Booking, RoomAvailability
from .forms import BookingForm
from django.shortcuts import render
from django.contrib.auth.models import User
from django.utils.dateparse import parse_date
from django.http import HttpResponseBadRequest
from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.contrib import messages


@login_required
def room_view(request):
    bookings = Booking.objects.filter(user=request.user)
    return render(request, 'booking_list.html', {'bookings': bookings})


@login_required
def create_booking(request):
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            booking = form.save(commit=False)
            booking.user = request.user  # Set the user field
            booking.save()
            messages.success(request, 'Booking has been created.')
            return redirect('booking_detail', pk=booking.pk)
    else:
        form = BookingForm()
    return render(request, 'create_booking.html', {'form': form})


def booking_detail(request, pk):
    booking = get_object_or_404(Booking, pk=pk)
    return render(request, 'booking_detail.html', {'booking': booking})

def update_booking(request, pk):
    booking = get_object_or_404(Booking, pk=pk)

    if request.method == 'POST':
        form = BookingForm(request.POST, instance=booking)
        if form.is_valid():
            form.save()
            messages.success(request, 'Booking has been updated.')
            return redirect('booking_detail', pk=pk)
        else:
            # If the form is not valid, display any errors
            messages.error(request, 'Please Enter The Room Number and Desired Check In and Check Out dates.')
    else:
        form = BookingForm(instance=booking)

    return render(request, 'update_booking.html', {'form': form, 'booking': booking})

def delete_booking(request, pk):
    booking = get_object_or_404(Booking, pk=pk)
    if request.method == 'POST':
        booking.delete()
        messages.success(request, 'Booking has been deleted.')

        return redirect('booking_list')
    return render(request, 'delete_booking.html', {'booking': booking})

def book_room(request, room_id):
    room_availability = RoomAvailability.objects.filter(room_id=room_id)
    
    if request.method == 'POST':
        form = BookingForm(request.POST)
        
        if form.is_valid():
            check_in_date = form.cleaned_data['check_in_date']
            check_out_date = form.cleaned_data['check_out_date']
            
            # Check if the room is available for the selected dates
            if room_availability.filter(date__range=[check_in_date, check_out_date]).exists():
                # Room is available, process the booking
                form.save()
                return HttpResponseRedirect(reverse('booking_success'))
            else:
                # Room is not available for the selected dates
                return render(request, 'room_not_available.html')
    else:
        form = BookingForm()

    return render(request, 'booking_form.html', {'form': form, 'room_availability': room_availability})

#def room(request):
 #   return render(request, 'room.html')
#def index(request):
 #   return HttpResponse("this is room page")
