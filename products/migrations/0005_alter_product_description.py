# Generated by Django 3.2.3 on 2021-08-16 18:34

from django.db import migrations
import djrichtextfield.models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0004_rename_name_category_url_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='description',
            field=djrichtextfield.models.RichTextField(),
        ),
    ]