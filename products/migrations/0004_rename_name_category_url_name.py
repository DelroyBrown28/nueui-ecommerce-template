# Generated by Django 3.2.3 on 2021-08-15 16:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_alter_product_category'),
    ]

    operations = [
        migrations.RenameField(
            model_name='category',
            old_name='name',
            new_name='url_name',
        ),
    ]