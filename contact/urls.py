from django.urls import path
from django.contrib.auth.views import LoginView  # Import LoginView from Django's authentication views
from . import views

# Define URL patterns for handling contact-related views
urlpatterns = [
    path('contacts/', views.contact_list, name='contact_list'),# URL pattern for listing contacts
    path('contacts/create/', views.contact_create, name='contact_create'),# URL pattern for creating a new contact
    path('contacts/<int:pk>/', views.contact_detail, name='contact_detail'),# URL pattern for viewing contact details
    path('contacts/<int:pk>/update/', views.contact_update, name='contact_update'),# URL pattern for updating contact details
    path('contacts/<int:pk>/delete/', views.contact_delete, name='contact_delete'),# URL pattern for deleting a contact
    path('login/', LoginView.as_view(), name='login'),# URL pattern for the login page
  
    
]
    
