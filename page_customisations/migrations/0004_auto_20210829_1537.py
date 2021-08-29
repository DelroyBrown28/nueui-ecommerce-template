# Generated by Django 3.2.3 on 2021-08-29 14:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('page_customisations', '0003_headercustomisation_edit_banner_buttons'),
    ]

    operations = [
        migrations.AddField(
            model_name='headercustomisation',
            name='id_tag',
            field=models.CharField(blank=True, default='small_banner_id', max_length=55, null=True),
        ),
        migrations.AlterField(
            model_name='homepagecustomisation',
            name='main_page_button_alignment',
            field=models.TextField(choices=[('text-align__left', 'Left'), ('text-align__center', 'Center'), ('text-align__right', 'Right')], default='text-align__left'),
        ),
        migrations.AlterField(
            model_name='homepagecustomisation',
            name='main_page_text_alignment',
            field=models.TextField(choices=[('text-align__left', 'Left'), ('text-align__center', 'Center'), ('text-align__right', 'Right')], default='text-align__left'),
        ),
    ]
