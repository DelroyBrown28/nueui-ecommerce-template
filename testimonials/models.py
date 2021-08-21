from django.db import models
from django.utils.html import mark_safe


class Testimonial(models.Model):
    name = models.CharField(max_length=100, blank=False, null=False)
    email = models.CharField(max_length=100, blank=True, null=True)
    your_thoughts = models.TextField(max_length=1000, blank=False, null=False)
    date_received = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
