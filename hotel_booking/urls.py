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
from django.contrib import admin
from django.urls import path, include
from home import views as index_views
from room import views as room_views
from contact import views as contact_views
from accounts import views as accounts_views



urlpatterns = [
    path('', index_views.index, name='index'),
    path('admin/', admin.site.urls),
    path('room/', room_views.index, name='room_index'),
    path('contact/', contact_views.index, name='contact_index'),
    path('accounts', accounts_views.index, name='accounts_index'),
    

]
