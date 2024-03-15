from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Contact(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone_number = models.CharField(max_length=15)
    address = models.TextField()
    message = models.TextField()  # New field for guest request

    def __str__(self):
        return self.name
