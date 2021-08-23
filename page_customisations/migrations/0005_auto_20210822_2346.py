# Generated by Django 3.2.3 on 2021-08-22 22:46

import colorfield.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('page_customisations', '0004_auto_20210822_1715'),
    ]

    operations = [
        migrations.AddField(
            model_name='testimonialspagecustomisation',
            name='form_field_border_color',
            field=colorfield.fields.ColorField(blank=True, default='#000000', max_length=18, null=True),
        ),
        migrations.AlterField(
            model_name='homepagecustomisation',
            name='main_page_button_alignment',
            field=models.TextField(choices=[('text-align__center', 'Center'), ('text-align__left', 'Left'), ('text-align__right', 'Right')], default='text-align__left'),
        ),
        migrations.AlterField(
            model_name='homepagecustomisation',
            name='main_page_text_alignment',
            field=models.TextField(choices=[('text-align__center', 'Center'), ('text-align__left', 'Left'), ('text-align__right', 'Right')], default='text-align__left'),
        ),
    ]
