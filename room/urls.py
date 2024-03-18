from django.urls import path
from . import views

urlpatterns = [
    #path('', views.booking_list, name='booking_list'),
    path('booking/create/', views.create_booking, name='create_booking'),
    path('booking/<int:pk>/', views.booking_detail, name='booking_detail'),
    path('booking/<int:pk>/update/', views.update_booking, name='update_booking'),
    path('booking/<int:pk>/delete/', views.delete_booking, name='delete_booking'),
    path('', views.room_view, name='room'),  
]