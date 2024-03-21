from django.db import models
from django.contrib.auth.models import User
# Create your models here.


# Define a model for storing contact information
class Contact(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone_number = models.CharField(max_length=15)
    address = models.TextField()
    message = models.TextField()  # New field for guest request
    created_on = models.DateTimeField(auto_now_add=True)  # Automatically set the current date and time when an object is created

    # Define a string representation for the Contact object
    def __str__(self):
        return self.name  # Return the name of the contact as the string representation
