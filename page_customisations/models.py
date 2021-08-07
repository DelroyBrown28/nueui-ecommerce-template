from django.db import models
from djrichtextfield.models import RichTextField
from colorfield.fields import ColorField


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
        blank=False, null=False, max_length=35, default="Name This Styling...")
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
    header_styling = models.CharField(
        blank=False, null=False, max_length=55, default="Default Styling")
    header_logo = models.ImageField(null=True, blank=True, upload_to='media')
    header_background_color = ColorField(format='hexa')
    search_icon_color = ColorField(format='hexa')
    search_icon_background_color = ColorField(format='hexa')
    small_banner_text = models.CharField(
        blank=False, null=False, max_length=100, default="Welcome")
    small_banner_background_color = ColorField(format='hexa')
    small_banner_text_color = ColorField(format='hexa')
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
        max_length=200, default='https://twitter.com/')
    linkedin_link = models.URLField(
        max_length=200, default='https://linkedin.com/')
    facebook_link = models.URLField(
        max_length=200, default='https://facebook.com/')
    instagram_link = models.URLField(
        max_length=200, default='https://instagram.com/')

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
    recipients_name = models.CharField(max_length=100, blank=False, null=False)

    twitter_link = models.URLField(blank=True, null=True,
                                   max_length=200, default='https://twitter.com/')
    linkedin_link = models.URLField(blank=True, null=True,
                                    max_length=200, default='https://linkedin.com/')
    facebook_link = models.URLField(blank=True, null=True,
                                    max_length=200, default='https://facebook.com/')
    instagram_link = models.URLField(blank=True, null=True,
                                     max_length=200, default='https://instagram.com/')

    testimonial = models.TextField(max_length=300, blank=False, null=False)

    class Meta:
        verbose_name_plural = '  Testimonials Page'

    def __str__(self):
        return self.recipients_name


class FooterCustomisation(models.Model):
    styling_name = models.CharField(
        blank=False, null=False, max_length=55, default="Default")
    background_color = ColorField(format='hex', default='#333333')
    text_color = ColorField(format='hex', default='#FFFFFF')

    twitter_link = models.URLField(
        max_length=200, blank=True, null=True, default='https://twitter.com/')
    linkedin_link = models.URLField(
        max_length=200, blank=True, null=True, default='https://linkedin.com/')
    facebook_link = models.URLField(
        max_length=200, blank=True, null=True, default='https://facebook.com/')
    instagram_link = models.URLField(
        max_length=200, blank=True, null=True, default='https://instagram.com/')

    social_media_icon_colors = ColorField(format='hex', default='FFFFFF')

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
