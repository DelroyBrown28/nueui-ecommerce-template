from django.db import models
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
        
class Product(models.Model):
    category = models.ForeignKey('Category', null=True, blank=True, on_delete=models.CASCADE)
    sku = models.CharField(max_length=254, null=True, blank=True)
    name = models.CharField(max_length=254)
    description = models.TextField()
    has_sizes = models.BooleanField(default=False, null=True, blank=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    rating = models.DecimalField(
        max_digits=6, decimal_places=2, null=True, blank=True)
    image_url = models.URLField(max_length=1024, blank=True, null=True)
    main_product_image = models.ImageField(null=True, blank=True, upload_to='product_images')
    small_image_1 = models.ImageField(null=True, blank=True, upload_to='product_images')
    small_image_2 = models.ImageField(null=True, blank=True, upload_to='product_images')
    
    def __str__(self):
        return self.name
    