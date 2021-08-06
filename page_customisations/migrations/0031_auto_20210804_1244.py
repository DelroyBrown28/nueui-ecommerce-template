# Generated by Django 3.2.3 on 2021-08-04 11:44

import colorfield.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('page_customisations', '0030_auto_20210804_1154'),
    ]

    operations = [
        migrations.AddField(
            model_name='globalsitestyling',
            name='dropdown_menu_background_color',
            field=colorfield.fields.ColorField(default='#FFFFFF', max_length=18),
        ),
        migrations.AddField(
            model_name='globalsitestyling',
            name='dropdown_menu_text_color',
            field=colorfield.fields.ColorField(default='#000000', max_length=18),
        ),
    ]