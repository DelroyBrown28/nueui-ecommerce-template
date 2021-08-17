# Generated by Django 3.2.3 on 2021-08-17 13:01

from django.db import migrations
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('page_customisations', '0009_auto_20210817_1400'),
    ]

    operations = [
        migrations.AlterField(
            model_name='footercustomisation',
            name='contact_number',
            field=phonenumber_field.modelfields.PhoneNumberField(blank=True, max_length=128, null=True, region=None),
        ),
    ]