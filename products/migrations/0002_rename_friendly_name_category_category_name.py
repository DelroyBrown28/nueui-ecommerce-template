# Generated by Django 3.2.3 on 2021-08-15 15:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='category',
            old_name='friendly_name',
            new_name='category_name',
        ),
    ]
