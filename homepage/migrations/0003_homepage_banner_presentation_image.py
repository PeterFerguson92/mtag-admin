# Generated by Django 4.2.1 on 2025-01-08 21:29

from django.db import migrations
import django_resized.forms
import homepage.uploadfiles


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0002_alter_aboutus_homepage_display_header_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='homepage',
            name='banner_presentation_image',
            field=django_resized.forms.ResizedImageField(blank=True, crop=None, force_format=None, keep_meta=True, null=True, quality=-1, scale=None, size=[1921, 905], upload_to=homepage.uploadfiles.homepage_background_upload_image_path, verbose_name='Banner Presentation Image'),
        ),
    ]
