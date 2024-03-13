from django.shortcuts import render

def room(request):
   return render(request, 'room.html')

def index(request):
   return render(request, 'home.html')

def contact(request):
   return render(request, 'contact.html')