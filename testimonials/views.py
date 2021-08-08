from django.shortcuts import render
from django.views.generic import ListView, TemplateView
from page_customisations.models import TestimonialsPageCustomisation


def testimonials(request):
    """Returns the Testimonials page."""

    testimonials = TestimonialsPageCustomisation.objects.all()
    context = {
        'testimonials' : testimonials,
    }
    return render(request, 'testimonials/testimonials.html', context)

