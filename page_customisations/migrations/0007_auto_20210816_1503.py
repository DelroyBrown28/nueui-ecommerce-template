# Generated by Django 3.2.3 on 2021-08-16 14:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('page_customisations', '0006_auto_20210815_1710'),
    ]

    operations = [
        migrations.CreateModel(
            name='CTACard',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('card_name', models.CharField(default='Default', max_length=100)),
                ('image', models.ImageField(upload_to='cta_card_images')),
                ('text', models.TextField()),
            ],
        ),
        migrations.AlterField(
            model_name='homepagecustomisation',
            name='home_page_styling',
            field=models.CharField(default='Default', max_length=35),
        ),
        migrations.AlterField(
            model_name='homepagecustomisation',
            name='main_page_button_alignment',
            field=models.TextField(choices=[('text-align__center', 'Center'), ('text-align__left', 'Left'), ('text-align__right', 'Right')], default='text-align__left'),
        ),
        migrations.AlterField(
            model_name='homepagecustomisation',
            name='main_page_text_alignment',
            field=models.TextField(choices=[('text-align__center', 'Center'), ('text-align__left', 'Left'), ('text-align__right', 'Right')], default='text-align__left'),
        ),
        migrations.AddField(
            model_name='homepagecustomisation',
            name='cta_card',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='page_customisations.ctacard'),
        ),
    ]
