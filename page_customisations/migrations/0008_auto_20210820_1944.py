# Generated by Django 3.2.3 on 2021-08-20 18:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('page_customisations', '0007_auto_20210820_1757'),
    ]

    operations = [
        migrations.AlterField(
            model_name='homepagecustomisation',
            name='main_page_button_alignment',
            field=models.TextField(choices=[('text-align__left', 'Left'), ('text-align__center', 'Center'), ('text-align__right', 'Right')], default='text-align__left'),
        ),
        migrations.AlterField(
            model_name='homepagecustomisation',
            name='main_page_text_alignment',
            field=models.TextField(choices=[('text-align__left', 'Left'), ('text-align__center', 'Center'), ('text-align__right', 'Right')], default='text-align__left'),
        ),
    ]
