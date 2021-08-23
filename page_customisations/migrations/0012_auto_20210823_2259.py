# Generated by Django 3.2.3 on 2021-08-23 21:59

import colorfield.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('page_customisations', '0011_auto_20210823_2143'),
    ]

    operations = [
        migrations.AddField(
            model_name='testimonialspagecustomisation',
            name='view_testimonial_button_background_color',
            field=colorfield.fields.ColorField(default='#FFFFFF', max_length=18),
        ),
        migrations.AddField(
            model_name='testimonialspagecustomisation',
            name='view_testimonial_button_border',
            field=models.TextField(blank=True, choices=[('add-border', 'Add Border'), ('no-border', 'No Border')], default='no-border', null=True),
        ),
        migrations.AddField(
            model_name='testimonialspagecustomisation',
            name='view_testimonial_button_border_color',
            field=colorfield.fields.ColorField(default='#000000', max_length=18),
        ),
        migrations.AddField(
            model_name='testimonialspagecustomisation',
            name='view_testimonial_button_label',
            field=models.CharField(default='', help_text='Button that drops you down to the Testimonials Form', max_length=55),
        ),
        migrations.AddField(
            model_name='testimonialspagecustomisation',
            name='view_testimonial_button_label_color',
            field=colorfield.fields.ColorField(default='#000000', max_length=18),
        ),
        migrations.AlterField(
            model_name='homepagecustomisation',
            name='main_page_button_alignment',
            field=models.TextField(choices=[('text-align__right', 'Right'), ('text-align__left', 'Left'), ('text-align__center', 'Center')], default='text-align__left'),
        ),
        migrations.AlterField(
            model_name='homepagecustomisation',
            name='main_page_text_alignment',
            field=models.TextField(choices=[('text-align__right', 'Right'), ('text-align__left', 'Left'), ('text-align__center', 'Center')], default='text-align__left'),
        ),
    ]
