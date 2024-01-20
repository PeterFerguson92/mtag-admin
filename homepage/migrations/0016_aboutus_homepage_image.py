# Generated by Django 4.2.1 on 2024-01-20 06:49

from django.db import migrations, models
import homepage.uploadfiles


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0015_homepage_banner_background_image_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='aboutus',
            name='homepage_image',
            field=models.ImageField(blank=True, null=True, upload_to=homepage.uploadfiles.homepage_about_us_cover_upload_image_path, verbose_name='Homepage Image'),
        ),
    ]
