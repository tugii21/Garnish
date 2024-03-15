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
from django.urls import path, include
from home import views as home_views
from room import views as room_views
from contact import views as contact_views
from accounts import views as accounts_views




urlpatterns = [
    path('', home_views.index, name='home'),
    path('admin/', admin.site.urls),
    path('room/', include('room.urls')),
    path("accounts/", include("allauth.urls")),
    path('summernote/', include('django_summernote.urls')),
    path('contact/', include('contact.urls')),
    #path('accounts/', accounts_views.index, name='signup'),
    #path('superuser/login/', accounts_views.superuser_login, name='superuser_login'),  # Check this line
    #path('dashboard/', views.dashboard, name='dashboard'),
    #path('room/', room_views.index, name='room_index'),
    #path('contact/', views.contact, name='contact'),
    #path('accounts/', accounts_views.index, name='login'),
    #path('accounts/', accounts_views.index, name='signup'),
]
    



  


