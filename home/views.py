from django.shortcuts import render

# Define the index view function
def index(request):
    """
    View function for the homepage.

    Args:
    - request: HttpRequest object representing the current HTTP request.

    Returns:
    - Rendered HTTP response with the 'home.html' template.
    """
    return render(request, 'home.html')


