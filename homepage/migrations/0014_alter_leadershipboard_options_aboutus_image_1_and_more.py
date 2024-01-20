# Generated by Django 4.2.1 on 2024-01-20 05:42

from django.db import migrations, models
import homepage.uploadfiles


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0013_leader_leadershipboard_homepage_leadershipboard'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='leadershipboard',
            options={'ordering': ('title', 'created_at'), 'verbose_name': 'Leadership Board', 'verbose_name_plural': 'Leadership Board'},
        ),
        migrations.AddField(
            model_name='aboutus',
            name='image_1',
            field=models.ImageField(blank=True, null=True, upload_to=homepage.uploadfiles.homepage_about_us_cover_upload_image_path, verbose_name='Image 1'),
        ),
        migrations.AddField(
            model_name='aboutus',
            name='image_2',
            field=models.ImageField(blank=True, null=True, upload_to=homepage.uploadfiles.homepage_about_us_cover_upload_image_path, verbose_name='Image 2'),
        ),
        migrations.AddField(
            model_name='aboutus',
            name='image_3',
            field=models.ImageField(blank=True, null=True, upload_to=homepage.uploadfiles.homepage_about_us_cover_upload_image_path, verbose_name='Image 3'),
        ),
        migrations.AddField(
            model_name='aboutus',
            name='image_4',
            field=models.ImageField(blank=True, null=True, upload_to=homepage.uploadfiles.homepage_about_us_cover_upload_image_path, verbose_name='Image 4'),
        ),
        migrations.AlterField(
            model_name='leader',
            name='description',
            field=models.TextField(max_length=700, verbose_name='Description'),
        ),
        migrations.AlterField(
            model_name='leader',
            name='role',
            field=models.CharField(max_length=300, verbose_name='Role'),
        ),
    ]
