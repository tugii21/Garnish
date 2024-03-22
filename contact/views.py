from django.shortcuts import render, redirect, get_object_or_404# Import necessary functions from Django's shortcuts module
from .models import Contact #import contact model from current dir model
from .forms import ContactForm #import contactform from forms
from django.contrib.auth.decorators import login_required # Import login_required decorator from Django's authentication decorators
from django.contrib import messages # Import messages module from Django's contrib package


@login_required # Decorator to ensure that only authenticated users can access this view
def contact_list(request):
    """
    Render a list of contacts associated with the authenticated user.

    If the user is authenticated, retrieve and display contacts belonging to the user.
    If not authenticated, retrieve and display all contacts.

    Parameters:
    request (HttpRequest): The HTTP request object.

    Returns:
    HttpResponse: Rendered HTML template displaying contact list.
    """
    if request.user.is_authenticated:
        contacts = Contact.objects.filter(user=request.user)
    else:
        # If not authenticated, get all contacts
        contacts = Contact.objects.all()
    return render(request, 'contact_list.html', {'contacts': contacts})



@login_required
def contact_detail(request, pk):
    """
    Render details of a specific contact associated with the authenticated user.

    Retrieve and display details of the contact with the specified primary key (pk)
    associated with the authenticated user.

    Parameters:
    request (HttpRequest): The HTTP request object.
    pk (int): Primary key of the contact to be displayed.

    Returns:
    HttpResponse: Rendered HTML template displaying contact details.
    """
    contact = get_object_or_404(Contact, pk=pk, user=request.user)
    return render(request, 'contact_detail.html', {'contact': contact})

@login_required
def contact_create(request):
    """
    Create a new contact associated with the authenticated user.

    If the request method is POST, process the form data to create a new contact.
    If the form is valid, save the contact associated with the authenticated user.
    If the request method is GET, display an empty form for contact creation.

    Parameters:
    request (HttpRequest): The HTTP request object.

    Returns:
    HttpResponse: Rendered HTML template displaying contact creation form.
    """
    if request.method == 'POST':
        # If the request method is POST, process the form data
        form = ContactForm(request.POST)
        if form.is_valid():
            # If the form is valid, save the contact associated with the authenticated user
            contact = form.save(commit=False)
            contact.user = request.user
            contact.save()
            messages.success(request, 'Your request has been sent.')
            return redirect('contact_list')
    else:
         # If the request method is GET, display the empty form
        form = ContactForm()
    return render(request, 'contact_form.html', {'form': form})

@login_required
def contact_update(request, pk):
    """
    Update an existing contact associated with the authenticated user.

    Retrieve the contact with the specified primary key (pk) associated with the authenticated user.
    If the request method is POST, process the form data to update the contact.
    If the form is valid, save the updated contact.
    If the request method is GET, display the form pre-filled with existing contact data.

    Parameters:
    request (HttpRequest): The HTTP request object.
    pk (int): Primary key of the contact to be updated.

    Returns:
    HttpResponse: Rendered HTML template displaying contact update form.
    """
    contact = get_object_or_404(Contact, pk=pk, user=request.user)
    if request.method == 'POST':
        # If the request method is POST, process the form data
        form = ContactForm(request.POST, instance=contact)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your request has been updated.')
            return redirect('contact_list')
    else:
        # If the request method is GET, display the form pre-filled with existing contact data
        form = ContactForm(instance=contact)
    return render(request, 'contact_form.html', {'form': form})

@login_required
def contact_delete(request, pk):
    """
    Delete an existing contact associated with the authenticated user.

    Retrieve the contact with the specified primary key (pk) associated with the authenticated user.
    If the request method is POST, delete the contact.
    If the request method is GET, display a confirmation page for contact deletion.

    Parameters:
    request (HttpRequest): The HTTP request object.
    pk (int): Primary key of the contact to be deleted.

    Returns:
    HttpResponse: Rendered HTML template displaying contact deletion confirmation.
    """
    contact = get_object_or_404(Contact, pk=pk, user=request.user)
    if request.method == 'POST':
        contact.delete()
        messages.success(request, 'Your request has been deleted successfully.')
        return redirect('contact_list')
    return render(request, 'contact_confirm_delete.html', {'contact': contact})





