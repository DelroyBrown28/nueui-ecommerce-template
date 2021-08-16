# Generated by Django 3.2.3 on 2021-08-16 15:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('page_customisations', '0011_ctacard_button_text'),
    ]

    operations = [
        migrations.RenameField(
            model_name='ctacard',
            old_name='button_text',
            new_name='button_label',
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
