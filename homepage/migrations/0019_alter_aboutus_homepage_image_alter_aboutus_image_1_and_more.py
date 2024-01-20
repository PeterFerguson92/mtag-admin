# Generated by Django 4.2.1 on 2024-01-20 23:48

from django.db import migrations, models
import homepage.uploadfiles


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0018_alter_leader_image_alter_video_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aboutus',
            name='homepage_image',
            field=models.ImageField(blank=True, null=True, upload_to=homepage.uploadfiles.homepage_about_us_cover_upload_image_path, validators=[homepage.uploadfiles.homepage_about_us_image_restriction], verbose_name='Homepage Image'),
        ),
        migrations.AlterField(
            model_name='aboutus',
            name='image_1',
            field=models.ImageField(blank=True, null=True, upload_to=homepage.uploadfiles.homepage_about_us_cover_upload_image_path, validators=[homepage.uploadfiles.about_us_image_restriction], verbose_name='Image 1'),
        ),
        migrations.AlterField(
            model_name='aboutus',
            name='image_2',
            field=models.ImageField(blank=True, null=True, upload_to=homepage.uploadfiles.homepage_about_us_cover_upload_image_path, validators=[homepage.uploadfiles.about_us_image_restriction], verbose_name='Image 2'),
        ),
        migrations.AlterField(
            model_name='aboutus',
            name='image_3',
            field=models.ImageField(blank=True, null=True, upload_to=homepage.uploadfiles.homepage_about_us_cover_upload_image_path, validators=[homepage.uploadfiles.about_us_image_restriction], verbose_name='Image 3'),
        ),
        migrations.AlterField(
            model_name='aboutus',
            name='image_4',
            field=models.ImageField(blank=True, null=True, upload_to=homepage.uploadfiles.homepage_about_us_cover_upload_image_path, validators=[homepage.uploadfiles.about_us_image_restriction], verbose_name='Image 4'),
        ),
        migrations.AlterField(
            model_name='banner',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=homepage.uploadfiles.homepage_banner_upload_image_path, validators=[homepage.uploadfiles.homepage_banner_image_restriction], verbose_name='Image'),
        ),
        migrations.AlterField(
            model_name='homepage',
            name='banner_background_image',
            field=models.ImageField(blank=True, null=True, upload_to=homepage.uploadfiles.homepage_background_upload_image_path, validators=[homepage.uploadfiles.homepage_background_image_restriction], verbose_name='Banner Background Image'),
        ),
        migrations.AlterField(
            model_name='homepage',
            name='leadership_board_background_image',
            field=models.ImageField(blank=True, null=True, upload_to=homepage.uploadfiles.homepage_background_upload_image_path, validators=[homepage.uploadfiles.homepage_background_image_restriction], verbose_name='Leadership Board Background Image'),
        ),
        migrations.AlterField(
            model_name='leader',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=homepage.uploadfiles.homepage_leader_cover_upload_image_path, validators=[homepage.uploadfiles.leader_image_restriction], verbose_name='Image'),
        ),
    ]
