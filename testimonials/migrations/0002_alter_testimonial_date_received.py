# Generated by Django 3.2.3 on 2021-08-18 15:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testimonials', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='testimonial',
            name='date_received',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]