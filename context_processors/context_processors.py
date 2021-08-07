from page_customisations.models import ProductsPageCustomisation
from page_customisations.views import (HeaderCustomisation,
                                       ProductsPageCustomisation,
                                       GlobalSiteStyling,
                                       FooterCustomisation,
                                       TestimonialsPageCustomisation)


def global_styles_processor(request):
    return {
       'global_styles': GlobalSiteStyling.objects.all(),
    }
    

def header_customisation_processor(request):
    return {
       'header_customisation': HeaderCustomisation.objects.all(),

    }

def footer_customisation_processor(request):
    return {
       'footer_customisation': FooterCustomisation.objects.all(),

    }

def testimonials_customisation_processor(request):
    return {
       'testimonials_customisation': TestimonialsPageCustomisation.objects.all(),

    }
    
def products_page_customisation_processor(request):
    return {
       'products_page_customisation': ProductsPageCustomisation.objects.all(),
    }
    
