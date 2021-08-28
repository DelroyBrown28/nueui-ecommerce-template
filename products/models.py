from django.db import models
from django.contrib.auth.models import User

from djrichtextfield.models import RichTextField
from django import forms


class Category(models.Model):

    class Meta:
        verbose_name = 'Categories'

    category_name = models.CharField(max_length=254, blank=False, null=False)
    url_name = models.CharField(max_length=254)

    def __str__(self):
        return self.url_name

    def get_category_name(self):
        return self.category_name


class SizePrice(models.Model):
    size_label = models.CharField(
        max_length=15, blank=True, null=True, default='', help_text='xs, s, m, l, xl')
    size_price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.size_label


class Product(models.Model):
    main_product_image = models.ImageField(
        null=False, blank=False, default='', upload_to='product_images', help_text='This will be the main image in the carousel.')
    alternative_image_1 = models.ImageField(
        null=True, blank=True, upload_to='product_images', help_text='This will be the first image in the carousel.')
    alternative_image_2 = models.ImageField(
        null=True, blank=True, upload_to='product_images', help_text='This will be the second image in the carousel.')
    category = models.ForeignKey(
        'Category', null=True, blank=True, help_text='Assign product to category', on_delete=models.CASCADE)
    # rating = models.DecimalField(
    #     max_digits=6, decimal_places=2, null=True, blank=True)
    sku = models.CharField(max_length=254, null=True, blank=True)
    name = models.CharField(max_length=254)
    description = RichTextField()
    has_sizes = models.BooleanField(default=False, null=True, blank=True)
    # price = models.DecimalField(max_digits=10, decimal_places=2)
    price = models.ForeignKey('SizePrice', on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.name
