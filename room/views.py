from django.shortcuts import render
#from django.http import HttpResponse

# Create your views here.

def room(request):
    return render(request, 'room.html')
#def room(request):
 #   return render(request, 'room.html')
#def index(request):
 #   return HttpResponse("this is room page")