from django.shortcuts import render, redirect, get_object_or_404# Import necessary functions from Django's shortcuts module
from .models import Contact
from .forms import ContactForm
from django.contrib.auth.decorators import login_required # Import login_required decorator from Django's authentication decorators
from django.contrib import messages # Import messages module from Django's contrib package


@login_required # Decorator to ensure that only authenticated users can access this view
def contact_list(request):
    # Check if the user is authenticated
    if request.user.is_authenticated:
        contacts = Contact.objects.filter(user=request.user)
    else:
        # If not authenticated, get all contacts
        contacts = Contact.objects.all()
    return render(request, 'contact_list.html', {'contacts': contacts})



@login_required
def contact_detail(request, pk):
    # Retrieve the contact with the specified primary key (pk) associated with the authenticated user
    contact = get_object_or_404(Contact, pk=pk, user=request.user)
    return render(request, 'contact_detail.html', {'contact': contact})

@login_required
def contact_create(request):
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
    # Retrieve the contact with the specified primary key (pk) associated with the authenticated user
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
    # Retrieve the contact with the specified primary key (pk) associated with the authenticated user
    contact = get_object_or_404(Contact, pk=pk, user=request.user)
    if request.method == 'POST':
        contact.delete()
        messages.success(request, 'Your request has been deleted successfully.')
        return redirect('contact_list')
    return render(request, 'contact_confirm_delete.html', {'contact': contact})





