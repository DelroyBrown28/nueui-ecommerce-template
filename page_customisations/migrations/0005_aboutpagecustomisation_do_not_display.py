# Generated by Django 3.2.3 on 2021-08-02 21:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('page_customisations', '0004_auto_20210802_2212'),
    ]

    operations = [
        migrations.AddField(
            model_name='aboutpagecustomisation',
            name='do_not_display',
            field=models.BooleanField(default=False, help_text='**Check this box to hide this specific styling.', verbose_name='Do not display'),
        ),
    ]