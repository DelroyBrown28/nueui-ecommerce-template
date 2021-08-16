from page_customisations.models import ProductsPageCustomisation, CTACard, CTABanner
from products.models import Category, Product
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


def cta_processor(request):
    return {
        'cta_customisation': CTACard.objects.all(),

    }


def cta_banner_processor(request):
    return {
        'cta_banner_customisation': CTABanner.objects.all(),

    }


def categories_processor(request):
    return {
        'categories_processor': Category.objects.all(),

    }


def products_processor(request):
    return {
        'products_processor': Product.objects.all(),

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
