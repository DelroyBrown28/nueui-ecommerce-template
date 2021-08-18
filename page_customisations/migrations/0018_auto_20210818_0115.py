# Generated by Django 3.2.3 on 2021-08-18 00:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('page_customisations', '0017_auto_20210817_2236'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aboutpagecustomisation',
            name='facebook_link',
            field=models.URLField(blank=True, default='https://facebook.com/', null=True),
        ),
        migrations.AlterField(
            model_name='aboutpagecustomisation',
            name='instagram_link',
            field=models.URLField(blank=True, default='https://instagram.com/', null=True),
        ),
        migrations.AlterField(
            model_name='aboutpagecustomisation',
            name='linkedin_link',
            field=models.URLField(blank=True, default='https://linkedin.com/', null=True),
        ),
        migrations.AlterField(
            model_name='aboutpagecustomisation',
            name='twitter_link',
            field=models.URLField(blank=True, default='https://twitter.com/', null=True),
        ),
        migrations.AlterField(
            model_name='homepagecustomisation',
            name='main_page_button_alignment',
            field=models.TextField(choices=[('text-align__left', 'Left'), ('text-align__right', 'Right'), ('text-align__center', 'Center')], default='text-align__left'),
        ),
        migrations.AlterField(
            model_name='homepagecustomisation',
            name='main_page_text_alignment',
            field=models.TextField(choices=[('text-align__left', 'Left'), ('text-align__right', 'Right'), ('text-align__center', 'Center')], default='text-align__left'),
        ),
    ]
