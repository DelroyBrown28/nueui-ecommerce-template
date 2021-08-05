# Generated by Django 3.2.3 on 2021-08-04 00:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('page_customisations', '0025_auto_20210804_0143'),
    ]

    operations = [
        migrations.AlterField(
            model_name='homepagecustomisation',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='home_page_images'),
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
