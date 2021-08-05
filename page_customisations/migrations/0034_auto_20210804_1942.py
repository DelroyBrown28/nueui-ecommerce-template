# Generated by Django 3.2.3 on 2021-08-04 18:42

import colorfield.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('page_customisations', '0033_auto_20210804_1912'),
    ]

    operations = [
        migrations.AddField(
            model_name='aboutpagecustomisation',
            name='contact_card_text_color',
            field=colorfield.fields.ColorField(default='#00000', max_length=18),
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
