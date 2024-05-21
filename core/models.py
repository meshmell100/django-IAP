from django.db import models
from django import forms

class ContactMessage(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.email}"

class Feedback(models.Model):
    names = models.CharField(max_length=100, blank=False)
    email = models.EmailField(blank=False)
    message = models.CharField(max_length=255, blank=False)  # Adjust the max_length as needed
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.names} - {self.email}"
