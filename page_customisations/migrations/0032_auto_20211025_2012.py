# Generated by Django 3.2.3 on 2021-10-25 19:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('page_customisations', '0031_auto_20211025_2011'),
    ]

    operations = [
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
        migrations.AlterField(
            model_name='testimonialspagecustomisation',
            name='form_field_borders',
            field=models.TextField(blank=True, choices=[('bottom-border', 'Bottom Border'), ('full-border', 'Full Border'), ('no-border', 'No Border')], default='no-border', null=True),
        ),
    ]
