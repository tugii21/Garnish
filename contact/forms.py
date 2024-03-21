from django import forms
from .models import Contact

# Define a form for handling contact information
class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact  # Set the model for the form to Contact
        fields = ['name', 'email', 'phone_number', 'address', 'message']