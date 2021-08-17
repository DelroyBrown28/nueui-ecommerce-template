# Generated by Django 3.2.3 on 2021-08-17 12:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('page_customisations', '0006_auto_20210816_2357'),
    ]

    operations = [
        migrations.AddField(
            model_name='footercustomisation',
            name='contact_number',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='footercustomisation',
            name='email',
            field=models.EmailField(blank=True, help_text='Enter your email to display in the footer.', max_length=254, null=True),
        ),
        migrations.AddField(
            model_name='footercustomisation',
            name='footer_logo',
            field=models.ImageField(blank=True, null=True, upload_to='footer_logo_images'),
        ),
        migrations.AlterField(
            model_name='homepagecustomisation',
            name='main_page_button_alignment',
            field=models.TextField(choices=[('text-align__right', 'Right'), ('text-align__center', 'Center'), ('text-align__left', 'Left')], default='text-align__left'),
        ),
        migrations.AlterField(
            model_name='homepagecustomisation',
            name='main_page_text_alignment',
            field=models.TextField(choices=[('text-align__right', 'Right'), ('text-align__center', 'Center'), ('text-align__left', 'Left')], default='text-align__left'),
        ),
    ]
