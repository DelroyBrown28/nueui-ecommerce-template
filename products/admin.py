from django.contrib import admin
from BasicTemplateMain.admin import superadmin

from .models import Product, Category


class ProductAdmin(admin.ModelAdmin):
    fieldsets = (
        ('Product Images', {
            'classes': ('fieldset_titles',),
            'fields': (
                'main_product_image',
                'alternative_image_1',
                'alternative_image_2',)

        }),
        ('Other', {
            "fields": (
                'name',
                'category',
                'price',
                'description',
                'has_sizes',)
        }),
    )
    search_fields = [
        'name',
        'sku',
        'price',
    ]
    list_filter = (
        'name',
        'category',
    )
    ordering = ('name',)

class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'category_name',
        'url_name',
    )
    list_display_links = ('category_name',)
    prepopulated_fields = {"url_name": ["category_name"]}
    
        

admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
