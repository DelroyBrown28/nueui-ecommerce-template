# Generated by Django 3.2.3 on 2021-08-25 16:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_sizeandprice_size_price_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sizeandprice',
            name='size_price_name',
            field=models.CharField(default='', max_length=25),
        ),
    ]
