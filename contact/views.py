from django.shortcuts import render
from django.http import HttpResponse

def contact(request):
    return render(request, 'contact.html')

# Create your views here.
#def index(request):
 #   return HttpResponse("Than you for contacting us, leave enquiries below")
