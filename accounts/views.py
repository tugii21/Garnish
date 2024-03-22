from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    """
    Render the index page of the account app.

    This view renders a simple message indicating that the user is in the account page
    and prompts them to log in or create an account.

    Parameters:
    request (HttpRequest): The HTTP request object.

    Returns:
    HttpResponse: Rendered HTML template displaying the index page message.
    """
    return HttpResponse("you are in Account page Log in or Creats")
