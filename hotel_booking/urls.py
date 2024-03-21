"""
URL configuration for hotel_booking project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from . import views
from django.contrib import admin
from django.urls import path, include # Import path function for defining URL patterns and include for including other URL configurations
from home import views as home_views  # Import views from the home app with an alias
from room import views as room_views
from contact import views as contact_views
from accounts import views as accounts_views



# Define urlpatterns as a list of URL patterns
urlpatterns = [
    path('', home_views.index, name='home'),
    path('admin/', admin.site.urls, name='admin'), # URL pattern for the Django admin interface
    path('room/', include('room.urls')),
    path("accounts/", include("allauth.urls")),
    path('summernote/', include('django_summernote.urls')), # Include URL patterns for django_summernote
    path('contact/', include('contact.urls')),
    
]
    



  


