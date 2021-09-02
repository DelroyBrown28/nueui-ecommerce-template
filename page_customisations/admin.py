from django.contrib import admin
from django.contrib.auth.models import User
from page_customisations.models import (HomePageCustomisation,
                                        HeaderCustomisation,
                                        ProductsPageCustomisation,
                                        GlobalSiteStyling,
                                        AboutPageCustomisation,
                                        FooterCustomisation,
                                        TestimonialsPageCustomisation,
                                        AddTestimonial,
                                        CTACard,
                                        CTABanner)
from BasicTemplateMain.admin import superadmin


# Superuser admin models
class AboutPageCustomisationAdmin(admin.ModelAdmin):
    fieldsets = (
        (None, {
            "fields": (
                'styling_name',)
        }),
        ('About Section', {
            'classes': ('fieldset_titles',),
            'fields': (
                'about_section_title',
                'about_section_blurb',
                'about_section_content',
                'about_section_left_image',
                'about_section_right_image'),

        }),
        ('Contact Section', {
            'classes': ('fieldset_titles',),
            'fields': (
                'contact_section_title',
                'contact_section_blurb',)

        }),
        ('Contact Card', {
            'classes': ('fieldset_titles',),
            'fields': (
                'contact_card_title',
                'contact_card_image',
                'contact_card_info',
                'contact_card_background_color',
                'contact_card_text_color',
                ('contact_card_border',
                 'border_color',),)

        }),
        ('Social Media Links', {
            'classes': ('fieldset_titles',),
            'fields': (
                ('twitter_link',
                 'linkedin_link'),
                ('facebook_link',
                 'instagram_link'),),
        }),

        ('Tick this box to HIDE these styles', {
            'classes': ('fieldset_titles',),
            'fields': (
                'do_not_display',),
        }),
    )
    list_display = (
        'styling_name',
        'do_not_display',
    )
    list_editable = (
        'do_not_display',
    )


class HomePageCustomisationAdmin(admin.ModelAdmin):
    fieldsets = (
        ('Home Page Styles', {
            "fields": (
                'home_page_styling',
                'image',)
        }),

        ('Main Text & Button Styles', {
            'classes': ('fieldset_titles', 'collapse in',),
            'fields': (
                'main_page_text',
                'main_page_text_alignment',
                'main_page_text_color',
                'button_text',
                'button_text_color',
                'button_background_color',
                'main_page_button_alignment',),

        }),
        ('Choose/Create your Call To Action Card', {
            'classes': ('fieldset_titles',),
            'fields': (
                'cta_card_1',
                'cta_card_2',),

        }),
        ('Choose/Create your Call To Action Banner', {
            'classes': ('fieldset_titles',),
            'fields': (
                'cta_banner',),
        }),

        ('Tick this box to HIDE these styles', {
            'classes': ('fieldset_titles',),
            'fields': (
                'do_not_display',),
        }),
    )
    list_display = (
        'home_page_styling',
        'do_not_display',
    )
    list_editable = (
        'do_not_display',

    )


class GlobalSiteStylingAdmin(admin.ModelAdmin):
    fieldsets = (
        ('Global Styles', {
            "fields": (
                'global_site_styles',
                'base_background_color',
                'base_font_color',
                'all_icon_colors',)
        }),
        ('Primary Button Styles', {
            'classes': ('fieldset_titles',),
            'fields': (
                ('primary_button_base_color',
                 'primary_button_text_color'),)

        }),
        ('Secondary Button Styles', {
            'classes': ('fieldset_titles',),
            'fields': (
                ('secondary_button_base_color',
                 'secondary_button_text_color'),)

        }),
        ('Pop up box styles', {
            'classes': ('fieldset_titles',),
            'fields': (
                ('pop_up_background_color',
                 'pop_up_text_color'),)
        }),
        ('Dropdown Menu Styles', {
            'classes': ('fieldset_titles',),
            'fields': (
                ('dropdown_menu_background_color',
                 'dropdown_menu_text_color'),)
        }),

        ('Tick this box to HIDE these styles', {
            'classes': ('fieldset_titles',),
            'fields': (
                'do_not_display',),
        }),
    )
    list_display = (
        'global_site_styles',
        'do_not_display',
    )
    list_editable = (
        'do_not_display',

    )


class HeaderCustomisationAdmin(admin.ModelAdmin):
    fieldsets = (
        ('Header Styling', {
            "fields": (
                'header_styling',
                'header_logo',
                'header_background_color',)
        }),
        ('Search icon and icon background', {
            'classes': ('fieldset_titles',),
            'fields': (
                ('search_icon_color',
                 'search_icon_background_color'),)

        }),
        ('Small Banner', {
            'classes': ('fieldset_titles',),
            'fields': (
                'small_banner_text',
                ('small_banner_background_color',
                 'small_banner_text_color',),)

        }),
        ('Small Banner Buttons', {
            'classes': ('fieldset_titles',),
            'fields': (
                'banner_button_label_1',
                'banner_button_url_link_1',
                'banner_button_label_2',
                'banner_button_url_link_2',
                'banner_button_background_color',
                'banner_button_label_color',
                'button_border',
                'button_border_color',),

        }),
        ('Small Banner Buttons (MOBILE)', {
            'classes': ('fieldset_titles',),
            'fields': (
                'mobile_banner_button_background_color',
                'mobile_banner_button_label_color',
                'mobile_button_border',
                'mobile_button_border_color',),

        }),

        ('Tick this box to HIDE these styles', {
            'classes': ('fieldset_titles',),
            'fields': (
                'do_not_display',),
        }),
    )
    radio_fields = {'button_border': admin.HORIZONTAL}
    list_display = (
        'header_styling',
        'do_not_display',
    )
    list_editable = (
        'do_not_display',

    )


class ProductsPageCustomisationAdmin(admin.ModelAdmin):
    fieldsets = (
        ('Products Page Styling', {
            "fields": (
                'products_page_styling',)
        }),
        ('Category Tag', {
            'classes': ('fieldset_titles',),
            'fields': (
                ('category_tag_border_color',
                 'category_tag_text_color'),)

        }),
        ('Product Cards', {
            'classes': ('fieldset_titles',),
            'fields': (
                'product_card_background_color',
                ('add_card_border',
                 'border_color'),
                'product_card_font_color',
                'product_card_icon_color',
                'product_quantity_button_background_color',
                'product_quantity_button_icon_color',)

        }),
        ('Tick this box to HIDE these styles', {
            'classes': ('fieldset_titles',),
            'fields': (
                'do_not_display',),
        }),
    )
    list_display = (
        'products_page_styling',
        'do_not_display',
    )
    list_editable = (
        'do_not_display',

    )


class FooterCustomisationAdmin(admin.ModelAdmin):
    fieldsets = (
        ('Footer Styles', {
            "fields": (
                'styling_name',)
        }),
        ('Background/text & icon colors', {
            'classes': ('fieldset_titles',),
            'fields': (
                'background_color',
                'footer_title_colors',
                'footer_text_color',
                'footer_icon_colors',
                'footer_top_border_color'),

        }),
        ('Footer Logo', {
            'classes': ('fieldset_titles',),
            'fields': (
                'footer_logo',),

        }),
        ('Contact Information', {
            'classes': ('fieldset_titles',),
            'fields': (
                'email',
                'contact_number',),

        }),
        ('Social Media Links & Colors', {
            'classes': ('fieldset_titles',),
            'fields': (
                ('twitter_link',
                 'linkedin_link'),
                ('facebook_link',
                 'instagram_link'),
                'social_media_icon_colors',
                'social_media_icon_background_color',),

        }),
    )
    list_display = (
        'styling_name',
        'do_not_display',
    )
    list_editable = (
        'do_not_display',

    )


class TestimonialsCustomisationAdmin(admin.ModelAdmin):
    fieldsets = (
        (None, {
            "fields": (
                'style_name',)
        }),

        ('Testimonial Card Styling', {
            'classes': ('fieldset_titles',),
            'fields': (
                'card_background_color',
                'card_border',
                'card_border_color',
                'card_font_color',
                'star_rating_color',
            ),
        }),
        ('Dropdown button', {
            'classes': ('fieldset_titles',),
            'fields': (
                'view_testimonial_button_label',
                'view_testimonial_button_label_color',
                'view_testimonial_button_background_color',
                'view_testimonial_button_border',
                'view_testimonial_button_border_color',
                'icon_color',
            ),
        }),
        ('Testimonial Form Styling', {
            'classes': ('fieldset_titles',),
            'fields': (
                'form_title',
                'testimonial_form_blurb',
                'form_background_color',
                'form_font_color',
                'form_field_border_color',
                'add_button_border',
                'submit_button_border_color',
                'submit_button_background_color',
                'submit_button_label',
                'submit_button_label_color',
            ),
        }),
    )
    list_display = (
        'style_name',
        'do_not_display',
    )
    list_editable = (
        'do_not_display',

    )


class AddTestimonialAdmin(admin.ModelAdmin):
    fieldsets = (
        (None, {
            "fields": (
                'recipients_name',)
        }),
        ('Customers Testimonial & Rating', {
            'classes': ('fieldset_titles',),
            'fields': (
                'testimonial',
                'customers_rating',
            ),
        }),
    )
    list_display = (
        'recipients_name',
        'customers_rating',
    )


class CTACardAdmin(admin.ModelAdmin):
    fieldsets = (
        ('CTA Card Styles', {
            "fields": (
                'cta_title',)
        }),
        ('CTA Text & Image', {
            'classes': ('fieldset_titles',),
            'fields': (
                'image',
                'cta_text',
                'cta_text_color',)

        }),
        ('CTA Button', {
            'classes': ('fieldset_titles',),
            'fields': (
                'button_label',
                ('button_background_color',
                 'button_label_color',),
                'add_button_border',
                'border_color',
                'button_url_choice',)
        }),
    )
    radio_fields = {'add_button_border': admin.HORIZONTAL}
    list_display = (
        'cta_title',
    )


class CTABannerAdmin(admin.ModelAdmin):
    fieldsets = (
        ('Banner Name', {
            "fields": (
                'banner_title',)
        }),
        ('CTA Banner Title & Styling', {
            'classes': ('fieldset_titles',),
            'fields': (
                'cta_banner_title',
                'banner_image',
                'banner_background_color',)
        }),
        ('CTA Banner Button', {
            'classes': ('fieldset_titles',),
            'fields': (
                'cta_button_label',
                ('label_color',
                 'button_background_color',),
                'add_button_border',
                'border_color',
                'cta_button_url',)
        }),

    )
    radio_fields = {'add_button_border': admin.HORIZONTAL}
    list_display = (
        'banner_title',
    )


"""
superadmin.register() to register for superuser admin
"""

superadmin.register(CTABanner, CTABannerAdmin)
superadmin.register(CTACard, CTACardAdmin)
superadmin.register(HomePageCustomisation, HomePageCustomisationAdmin)
superadmin.register(AddTestimonial, AddTestimonialAdmin)
superadmin.register(TestimonialsPageCustomisation,
                    TestimonialsCustomisationAdmin)
superadmin.register(FooterCustomisation, FooterCustomisationAdmin)
superadmin.register(HeaderCustomisation, HeaderCustomisationAdmin)
superadmin.register(ProductsPageCustomisation, ProductsPageCustomisationAdmin)
superadmin.register(GlobalSiteStyling, GlobalSiteStylingAdmin)
superadmin.register(AboutPageCustomisation, AboutPageCustomisationAdmin)
superadmin.register(User)
