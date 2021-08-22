from django.db import models
from products.models import Product
from django.utils.html import mark_safe



class Testimonial(models.Model):
    """
    This model is for the customers on the frontend.
    And also in the admin
    """
    name = models.CharField(max_length=100, blank=False, null=False)
    email = models.CharField(max_length=100, blank=True, null=True)
    your_thoughts = models.TextField(max_length=1000, blank=False, null=False)
    rating = models.CharField(max_length=1, null=True, blank=True)
    date_received = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Customer testimonial from {self.name}"
