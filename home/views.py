from django.shortcuts import render


def index(request):
    return render(request, 'home.html')


#from django.shortcuts import render
#from django.http import HttpResponse

# Create your views here.
#def index(request):
 #   return HttpResponse("Welcome to Garnish B&b")

