from django.urls import path
from . import views

# Define URL patterns for booking-related views
urlpatterns = [
    path('booking/create/', views.create_booking, name='create_booking'),    # URL pattern for creating a new booking
    path('booking/<int:pk>/', views.booking_detail, name='booking_detail'),    # URL pattern for viewing details of a specific booking by its primary key
    path('booking/<int:pk>/update/', views.update_booking, name='update_booking'),     # URL pattern for updating a booking by its primary key
    path('booking/<int:pk>/delete/', views.delete_booking, name='delete_booking'),    # URL pattern for deleting a booking by its primary key
    path('', views.room_view, name='room'),  # Display all bookings
    path('booking/list/', views.room_view, name='booking_list'),# Display user-specific bookings

]