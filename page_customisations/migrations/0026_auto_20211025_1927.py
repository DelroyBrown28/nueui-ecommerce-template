# Generated by Django 3.2.3 on 2021-10-25 18:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('page_customisations', '0025_auto_20211024_2319'),
    ]

    operations = [
        migrations.RenameField(
            model_name='aboutpagecustomisation',
            old_name='about_page_content',
            new_name='story_of_your_brand',
        ),
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