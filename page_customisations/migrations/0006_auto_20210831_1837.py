# Generated by Django 3.2.3 on 2021-08-31 17:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('page_customisations', '0005_auto_20210831_1835'),
    ]

    operations = [
        migrations.AlterField(
            model_name='headercustomisation',
            name='banner_button_label_1',
            field=models.CharField(blank=True, default='', max_length=25, null=True),
        ),
        migrations.AlterField(
            model_name='headercustomisation',
            name='banner_button_label_2',
            field=models.CharField(blank=True, default='', max_length=25, null=True),
        ),
    ]