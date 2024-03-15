from django.shortcuts import render, redirect, get_object_or_404
from .models import Contact
from .forms import ContactForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages


@login_required
def contact_list(request):
    contacts = Contact.objects.filter(user=request.user)
    return render(request, 'contact_list.html', {'contacts': contacts})



@login_required
def contact_detail(request, pk):
    contact = get_object_or_404(Contact, pk=pk, user=request.user)
    return render(request, 'contact_detail.html', {'contact': contact})

@login_required
def contact_create(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            contact = form.save(commit=False)
            contact.user = request.user
            contact.save()
            messages.success(request, 'Your request has been sent.')
            return redirect('contact_list')
    else:
        form = ContactForm()
    return render(request, 'contact_form.html', {'form': form})

@login_required
def contact_update(request, pk):
    contact = get_object_or_404(Contact, pk=pk, user=request.user)
    if request.method == 'POST':
        form = ContactForm(request.POST, instance=contact)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your request has been updated.')
            return redirect('contact_list')
    else:
        form = ContactForm(instance=contact)
    return render(request, 'contact_form.html', {'form': form})

@login_required
def contact_delete(request, pk):
    contact = get_object_or_404(Contact, pk=pk, user=request.user)
    if request.method == 'POST':
        contact.delete()
        messages.success(request, 'Your request has been deleted successfully.')
        return redirect('contact_list')
    return render(request, 'contact_confirm_delete.html', {'contact': contact})


@login_required
def contact_list(request):
    contacts = Contact.objects.all()
    return render(request, 'contact_list.html', {'contacts': contacts})