from django.db import models
from django.db.models.fields import EmailField
from django.db.models.fields.json import HasKeyLookup
from products.models import Category
from django.utils.html import mark_safe
from djrichtextfield.models import RichTextField
from colorfield.fields import ColorField
from phonenumber_field.modelfields import PhoneNumberField


class GlobalSiteStyling(models.Model):
    SITE_BORDERS = (
        ('add-border', 'Add Border'),
        ('no-border', 'No Border'),
    )
    global_site_styles = models.CharField(
        blank=False, null=False, max_length=20, help_text="Give these global styles a name...")
    base_background_color = ColorField(format='hex', default='#FFFFFF')
    base_font_color = ColorField(format='hex', default='#000000')
    all_icon_colors = ColorField(format='hex', default='#000000')
    primary_button_base_color = ColorField(format='hex', default='#000000')
    primary_button_text_color = ColorField(format='hex', default='#000000')
    secondary_button_base_color = ColorField(format='hex', default='#000000')
    secondary_button_text_color = ColorField(format='hex', default='#000000')
    pop_up_background_color = ColorField(format='hex', default='#FFFFFF')
    pop_up_text_color = ColorField(format='hex', default='#000000')
    dropdown_menu_background_color = ColorField(
        format='hex', default='#FFFFFF')
    dropdown_menu_text_color = ColorField(format='hex', default='#000000')

    do_not_display = models.BooleanField(verbose_name='Do not display',
                                         default=False,
                                         help_text='Check this box to hide this specific styling.')

    class Meta:
        verbose_name_plural = '        Global Page Styles'

    def save(self, *args, **kwargs):
        if self.do_not_display == False:
            try:
                temp = GlobalSiteStyling.objects.get(do_not_display=False)
                if self != temp:
                    temp.do_not_display = True
                    temp.save()
            except GlobalSiteStyling.DoesNotExist:
                pass
        super(GlobalSiteStyling, self).save(*args, **kwargs)

    def __str__(self):
        return self.global_site_styles


class CTACard(models.Model):
    ADD_BUTTON_BORDER = (
        ('add-border', 'Add Border'),
        ('no-border', 'Remove Border'),
    )
    image = models.ImageField(null=False, blank=False,
                              upload_to='cta_card_images')
    cta_title = models.CharField(
        blank=False, null=False, max_length=100, default="Default")
    cta_title_text_color = ColorField(format='hexa', default='#000000')
    cta_text = RichTextField()
    button_url_choice = models.ForeignKey('products.Category', null=True, blank=True, related_name='button_url',
                                          on_delete=models.CASCADE, help_text="Connect to one of your categories")
    button_label = models.CharField(max_length=25, blank=False, null=False)
    button_background_color = ColorField(format='hexa', default='#000000')
    button_label_color = ColorField(format='hexa', default='#FFFFFF')
    add_button_border = models.TextField(choices=ADD_BUTTON_BORDER,
                                         blank=False,
                                         null=False,
                                         default="no-border")
    border_color = ColorField(format='hexa', default='#000000')

    def __str__(self):
        return self.cta_title


class CTABanner(models.Model):
    ADD_BUTTON_BORDER = (
        ('add-border', 'Add Border'),
        ('no-border', 'Remove Border'),
    )
    banner_title = models.CharField(
        max_length=25, blank=False, null=False, default='default', help_text='Banner Name')
    cta_banner_title = RichTextField(default="")
    cta_button_label = models.CharField(
        max_length=25, null=False, blank=False, default="")
    label_color = ColorField(format='hexa', default='#FFFFFF')
    add_button_border = models.TextField(
        choices=ADD_BUTTON_BORDER, blank=False, null=False, default='no-border')
    border_color = ColorField(format='hexa', default='#000000')
    button_background_color = ColorField(format='hexa', default='#000000')
    cta_button_url = models.URLField(max_length=500, blank=True, null=True)
    banner_background_color = ColorField(format='hexa', default='#000000')

    def __str__(self):
        return self.banner_title


class HomePageCustomisation(models.Model):
    TEXT_ALIGNMENT_CHOICES = {
        ('text-align__right', 'Right'),
        ('text-align__left', 'Left'),
        ('text-align__center', 'Center'),
    }
    BUTTON_ALIGNMENT_CHOICES = {
        ('text-align__right', 'Right'),
        ('text-align__left', 'Left'),
        ('text-align__center', 'Center'),
    }
    home_page_styling = models.CharField(
        blank=False, null=False, max_length=35, default="Default")
    image = models.ImageField(null=True, blank=True,
                              upload_to='home_page_images')
    main_page_text = RichTextField()
    main_page_text_alignment = models.TextField(
        choices=TEXT_ALIGNMENT_CHOICES, blank=False, null=False, default='text-align__left')
    main_page_text_color = ColorField(format='hexa')
    button_text = models.CharField(
        blank=False, null=False, max_length=15, default='Shop Now')
    button_text_color = ColorField(format='hexa')
    button_background_color = ColorField(format='hexa')
    main_page_button_alignment = models.TextField(
        choices=BUTTON_ALIGNMENT_CHOICES, blank=False, null=False, default='text-align__left')
    cta_card_1 = models.ForeignKey(
        'CTACard', null=True, blank=True, related_name='cta_card_1', on_delete=models.CASCADE)
    cta_card_2 = models.ForeignKey(
        'CTACard', null=True, blank=True, related_name='cta_card_2', on_delete=models.CASCADE)
    cta_banner = models.ForeignKey(
        'CTABanner', null=True, blank=True, related_name='cta_banner', on_delete=models.CASCADE)
    do_not_display = models.BooleanField(verbose_name='Do not display',
                                         default=False,
                                         help_text='CHECK THIS BOX TO HIDE THIS SPECIFIC STYLING.')

    class Meta:
        verbose_name_plural = '     Home Page'

    def save(self, *args, **kwargs):
        if self.do_not_display == False:
            try:
                temp = HomePageCustomisation.objects.get(do_not_display=False)
                if self != temp:
                    temp.do_not_display = True
                    temp.save()
            except HomePageCustomisation.DoesNotExist:
                pass
        super(HomePageCustomisation, self).save(*args, **kwargs)

    def __str__(self):
        return self.home_page_styling


class HeaderCustomisation(models.Model):
    ADD_BUTTON_BORDER = (
        ('add-border', 'Add Border'),
        ('no-border', 'Remove Border'),
    )
    header_styling = models.CharField(
        blank=False, null=False, max_length=55, default="Default Styling")
    header_logo = models.ImageField(null=True, blank=True, upload_to='media')
    header_background_color = ColorField(format='hexa')
    search_icon_color = ColorField(format='hexa')
    search_icon_background_color = ColorField(format='hexa')
    small_banner_text = RichTextField()
    small_banner_background_color = ColorField(format='hexa')
    small_banner_text_color = ColorField(format='hexa')
    banner_button_label_1 = models.CharField(
        default='', blank=False, null=False, max_length=25)
    banner_button_url_link_1 = models.URLField(
        blank=True, null=True, max_length=250)
    banner_button_label_2 = models.CharField(
        default='', blank=False, null=False, max_length=25)
    banner_button_url_link_2 = models.URLField(
        blank=True, null=True, max_length=250)
    banner_button_background_color = ColorField(
        format='hexa', default='#FFFFFF')
    banner_button_label_color = ColorField(format='hexa', default='#000000')
    button_border = models.TextField(
        choices=ADD_BUTTON_BORDER, null=True, blank=True, default='no-border')
    button_border_color = ColorField(format='hexa', default='#000000')
    mobile_banner_button_background_color = ColorField(
        format='hexa', default='#FFFFFF')
    mobile_banner_button_label_color = ColorField(
        format='hexa', default='#000000')
    mobile_button_border = models.TextField(
        choices=ADD_BUTTON_BORDER, null=True, blank=True, default='no-border')
    mobile_button_border_color = ColorField(format='hexa', default='#000000')
    do_not_display = models.BooleanField(verbose_name='Do not display',
                                         default=False,
                                         help_text='CHECK THIS BOX TO HIDE THIS SPECIFIC STYLING.')

    class Meta:
        verbose_name_plural = '      Header'

    def save(self, *args, **kwargs):
        if self.do_not_display == False:
            try:
                temp = HeaderCustomisation.objects.get(do_not_display=False)
                if self != temp:
                    temp.do_not_display = True
                    temp.save()
            except HeaderCustomisation.DoesNotExist:
                pass
        super(HeaderCustomisation, self).save(*args, **kwargs)

    def __str__(self):
        return self.header_styling


class ProductsPageCustomisation(models.Model):
    BORDER_SIZE_CHOICES = (
        ('add-border', 'Add Border'),
        ('no-border', 'No Border'),
    )
    products_page_styling = models.CharField(
        blank=False, null=False, max_length=55, default="Default Product Page Styling")
    category_tag_border_color = ColorField(format='hexa')
    category_tag_text_color = ColorField(format='hexa')
    product_card_background_color = ColorField(format='hexa')
    add_card_border = models.TextField(choices=BORDER_SIZE_CHOICES,
                                       blank=False,
                                       null=False,
                                       default="no-border")
    border_color = ColorField(format='hexa')
    product_card_font_color = ColorField(format='hex')
    product_card_icon_color = ColorField(format='hexa')
    product_quantity_buttons = ColorField(
        format='hexa', help_text="**Product Display Page")
    do_not_display = models.BooleanField(verbose_name='Do not display',
                                         default=False,
                                         help_text='**Check this box to hide this specific styling.')

    class Meta:
        verbose_name_plural = '    Products Page'

    def save(self, *args, **kwargs):
        if self.do_not_display == False:
            try:
                temp = ProductsPageCustomisation.objects.get(
                    do_not_display=False)
                if self != temp:
                    temp.do_not_display = True
                    temp.save()
            except ProductsPageCustomisation.DoesNotExist:
                pass
        super(ProductsPageCustomisation, self).save(*args, **kwargs)

    def __str__(self):
        return self.products_page_styling


class AboutPageCustomisation(models.Model):
    ADD_BORDER = (
        ('add-contact-card-border', 'Add Border'),
        ('no-border', 'No Border'),
    )
    styling_name = models.CharField(
        blank=False, null=False, max_length=55, default="Default")
    about_section_title = models.CharField(
        max_length=100, blank=False, null=False)
    about_section_blurb = models.TextField(
        max_length=250, blank=False, null=False, default='Short blurb')
    about_section_content = RichTextField()
    about_section_left_image = models.ImageField(
        null=True, blank=True, upload_to='about_page_images')
    about_section_right_image = models.ImageField(
        null=True, blank=True, upload_to='about_page_images')

    contact_section_title = models.CharField(
        max_length=100, blank=False, null=False)
    contact_section_blurb = models.TextField(
        max_length=250, blank=False, null=False, default='Short blurb')
    contact_card_title = models.CharField(
        max_length=100, blank=False, null=False, default='Business Name')
    contact_card_info = RichTextField()
    contact_card_image = models.ImageField(
        null=True, blank=True, upload_to='about_page_images/contact_page_images')
    contact_card_background_color = ColorField(format='hex', default='#FFFFFF')
    contact_card_text_color = ColorField(format='hex', default='#00000')
    contact_card_border = models.TextField(choices=ADD_BORDER,
                                           blank=False,
                                           null=False,
                                           default="no-border")
    border_color = ColorField(format='hexa')

    twitter_link = models.URLField(
        max_length=200, null=True, blank=True, default='https://twitter.com/')
    linkedin_link = models.URLField(
        max_length=200, null=True, blank=True, default='https://linkedin.com/')
    facebook_link = models.URLField(
        max_length=200, null=True, blank=True, default='https://facebook.com/')
    instagram_link = models.URLField(
        max_length=200, null=True, blank=True, default='https://instagram.com/')

    do_not_display = models.BooleanField(verbose_name='Do not display',
                                         default=False,
                                         help_text='**Check this box to hide this specific styling.')

    class Meta:
        verbose_name_plural = '  About Page'

    def save(self, *args, **kwargs):
        if self.do_not_display == False:
            try:
                temp = AboutPageCustomisation.objects.get(do_not_display=False)
                if self != temp:
                    temp.do_not_display = True
                    temp.save()
            except AboutPageCustomisation.DoesNotExist:
                pass
        super(AboutPageCustomisation, self).save(*args, **kwargs)

    def __str__(self):
        return self.styling_name





class TestimonialsPageCustomisation(models.Model):
    """
    This model is to ADD testimonials to the page
    """
    TESTIMONIAL_CARD_BORDER = (
        ('add-border', 'Add Border'),
        ('no-border', 'No Border'),
    )
    recipients_name = models.CharField(max_length=100, blank=False, null=False)
    testimonial = RichTextField(blank=False, null=False, max_length=500)
    customers_rating = models.CharField(max_length=1, blank=True, null=True)
    card_background_color = ColorField(format='hexa', blank=True, null=True, default='#FFFFFF')
    card_border = models.TextField(choices=TESTIMONIAL_CARD_BORDER, blank=True, null=True, default='no-border')
    card_border_color = ColorField(format='hexa', blank=True, null=True, default='#FFFFFF')
    card_font_color = ColorField(format='hexa', blank=True, null=True, default='#000000')
    star_rating_color = ColorField(format='hexa', blank=True, null=True, default='#FFFF00')

    class Meta:
            verbose_name_plural = '  Testimonials Page'

    def __str__(self):
        return self.recipients_name


class FooterCustomisation(models.Model):
    styling_name = models.CharField(
        blank=False, null=False, max_length=55, default="Default")
    background_color = ColorField(format='hex', default='#333333')
    text_color = ColorField(format='hex', default='#FFFFFF')
    footer_logo = models.ImageField(
        null=True, blank=True, upload_to='footer_logo_images')
    footer_top_border_color = ColorField(format='hex', default='#000000')

    twitter_link = models.URLField(
        max_length=200, blank=True, null=True, default='https://twitter.com/')
    linkedin_link = models.URLField(
        max_length=200, blank=True, null=True, default='https://linkedin.com/')
    facebook_link = models.URLField(
        max_length=200, blank=True, null=True, default='https://facebook.com/')
    instagram_link = models.URLField(
        max_length=200, blank=True, null=True, default='https://instagram.com/')

    social_media_icon_colors = ColorField(format='hex', default='FFFFFF')
    email = models.EmailField(
        null=True, blank=True, help_text='Enter your email to display in the footer.')
    contact_number = PhoneNumberField(null=True, blank=True)

    do_not_display = models.BooleanField(verbose_name='Do not display',
                                         default=False,
                                         help_text='**Check this box to hide this specific styling.')

    class Meta:
        verbose_name_plural = ' Footer'

    def save(self, *args, **kwargs):
        if self.do_not_display == False:
            try:
                temp = FooterCustomisation.objects.get(do_not_display=False)
                if self != temp:
                    temp.do_not_display = True
                    temp.save()
            except FooterCustomisation.DoesNotExist:
                pass
        super(FooterCustomisation, self).save(*args, **kwargs)

    def __str__(self):
        return self.styling_name
