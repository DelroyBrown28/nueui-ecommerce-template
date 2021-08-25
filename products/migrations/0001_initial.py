# Generated by Django 3.2.3 on 2021-08-25 16:41

from django.db import migrations, models
import django.db.models.deletion
import djrichtextfield.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category_name', models.CharField(max_length=254)),
                ('url_name', models.CharField(max_length=254)),
            ],
            options={
                'verbose_name': 'Categories',
            },
        ),
        migrations.CreateModel(
            name='SizeAndPrice',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('size_label_1', models.CharField(blank=True, default='', help_text='s, m, l', max_length=15, null=True)),
                ('size_price_1', models.DecimalField(decimal_places=2, max_digits=6)),
                ('size_label_2', models.CharField(blank=True, default='', help_text='s, m, l', max_length=15, null=True)),
                ('size_price_2', models.DecimalField(decimal_places=2, max_digits=6)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('main_product_image', models.ImageField(default='', help_text='This will be the main image in the carousel.', upload_to='product_images')),
                ('alternative_image_1', models.ImageField(blank=True, help_text='This will be the first image in the carousel.', null=True, upload_to='product_images')),
                ('alternative_image_2', models.ImageField(blank=True, help_text='This will be the second image in the carousel.', null=True, upload_to='product_images')),
                ('sku', models.CharField(blank=True, max_length=254, null=True)),
                ('name', models.CharField(max_length=254)),
                ('description', djrichtextfield.models.RichTextField()),
                ('has_sizes', models.BooleanField(blank=True, default=False, null=True)),
                ('category', models.ForeignKey(blank=True, help_text='Assign product to category', null=True, on_delete=django.db.models.deletion.CASCADE, to='products.category')),
                ('price', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.sizeandprice')),
            ],
        ),
    ]
