# Generated by Django 3.2.3 on 2021-08-17 19:56

import colorfield.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('page_customisations', '0013_auto_20210817_2053'),
    ]

    operations = [
        migrations.AddField(
            model_name='headercustomisation',
            name='button_border_color',
            field=colorfield.fields.ColorField(default='#000000', max_length=18),
        ),
    ]
