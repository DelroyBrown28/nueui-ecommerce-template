# Generated by Django 3.2.3 on 2021-08-19 17:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testimonials', '0004_testimonial_upload_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='testimonial',
            name='upload_image',
            field=models.ImageField(blank=True, help_text='Show us an image of your purchased product', null=True, upload_to='media/testimonial_submitted_images'),
        ),
    ]
