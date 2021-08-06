from django.contrib import admin
from BasicTemplateMain.admin import superadmin

from .models import Product, Category


class ProductAdmin(admin.ModelAdmin):
    fieldsets = (
        (None, {
            "fields": (
                'name',
                'category',
                'price',
                'has_sizes',
                'rating',)
        }),
        ('Product Images', {
            'classes': ('fieldset_titles',),
            'fields': (
                'main_product_image',
                'small_image_1',
                'small_image_2',)

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
        'friendly_name',
        'name',
    )
    list_display_links = ('name',)
    list_editable = (
        'friendly_name',
    )
    
        

admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
