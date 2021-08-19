# Generated by Django 3.2.3 on 2021-08-19 12:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testimonials', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='testimonial',
            old_name='full_name',
            new_name='name',
        ),
        migrations.AddField(
            model_name='testimonial',
            name='email',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='testimonial',
            name='upload_image',
            field=models.ImageField(blank=True, help_text='Show us an image of your purchased product', null=True, upload_to='testimonial_submitted_images'),
        ),
        migrations.AlterField(
            model_name='testimonial',
            name='your_thoughts',
            field=models.TextField(max_length=1000),
        ),
    ]