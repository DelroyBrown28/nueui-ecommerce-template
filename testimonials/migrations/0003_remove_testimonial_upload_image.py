# Generated by Django 3.2.3 on 2021-08-19 13:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('testimonials', '0002_auto_20210819_1345'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='testimonial',
            name='upload_image',
        ),
    ]
