# Generated by Django 4.2.1 on 2024-01-17 14:19

import activities.uploadfiles
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('activities', '0007_remove_event_end_time_remove_event_start_time_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='cover_image_path',
            field=models.ImageField(blank=True, null=True, upload_to=activities.uploadfiles.event_upload_image_path, verbose_name='Cover image'),
        ),
        migrations.AddField(
            model_name='event',
            name='location',
            field=models.CharField(default='', max_length=255, verbose_name='Location'),
            preserve_default=False,
        ),
    ]