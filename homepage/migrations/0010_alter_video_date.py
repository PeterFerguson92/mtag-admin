# Generated by Django 4.2.1 on 2024-01-19 20:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0009_video_alter_aboutus_homepage_display_info_1_text_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='video',
            name='date',
            field=models.DateField(blank=True, null=True, verbose_name='Date'),
        ),
    ]