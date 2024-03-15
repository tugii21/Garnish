from django.urls import path
from . import views

urlpatterns = [
    path('', views.room, name='room'),
]

#from . import views
#urlpatterns=[Path('room',views.room, name='roompage'),]