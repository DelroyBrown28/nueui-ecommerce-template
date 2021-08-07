from django.shortcuts import render
from django.views.generic import ListView, TemplateView
# from page_customisations.models import HomePageCustomisation


def testimonials(request):
    """Returns the Testimonials page."""
    # home_page_customisation = HomePageCustomisation.objects.all()
    # context = {
    #     'home_page_customisation' : home_page_customisation,
    # }
    return render(request, 'testimonials/testimonials.html') #TODO: Add 'context'


