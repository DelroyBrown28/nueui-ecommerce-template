# Generated by Django 3.2.3 on 2021-08-17 13:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('page_customisations', '0008_auto_20210817_1355'),
    ]

    operations = [
        migrations.AlterField(
            model_name='homepagecustomisation',
            name='main_page_button_alignment',
            field=models.TextField(choices=[('text-align__center', 'Center'), ('text-align__right', 'Right'), ('text-align__left', 'Left')], default='text-align__left'),
        ),
        migrations.AlterField(
            model_name='homepagecustomisation',
            name='main_page_text_alignment',
            field=models.TextField(choices=[('text-align__center', 'Center'), ('text-align__right', 'Right'), ('text-align__left', 'Left')], default='text-align__left'),
        ),
    ]