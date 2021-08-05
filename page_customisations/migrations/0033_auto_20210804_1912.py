# Generated by Django 3.2.3 on 2021-08-04 18:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('page_customisations', '0032_auto_20210804_1610'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='aboutpagecustomisation',
            options={'verbose_name_plural': 'About Page'},
        ),
        migrations.AlterModelOptions(
            name='globalsitestyling',
            options={'verbose_name_plural': '    Global Page Styles'},
        ),
        migrations.AlterModelOptions(
            name='headercustomisation',
            options={'verbose_name_plural': '   Header'},
        ),
        migrations.AlterModelOptions(
            name='homepagecustomisation',
            options={'verbose_name_plural': '  Home Page'},
        ),
        migrations.AlterModelOptions(
            name='productspagecustomisation',
            options={'verbose_name_plural': '  Products Page'},
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
