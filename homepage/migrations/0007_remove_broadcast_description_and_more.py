# Generated by Django 4.2.1 on 2024-02-17 16:40

from django.db import migrations, models
import homepage.uploadfiles


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0006_alter_broadcast_subtitle'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='broadcast',
            name='description',
        ),
        migrations.AddField(
            model_name='broadcast',
            name='StreamDescription',
            field=models.TextField(blank=True, max_length=230, null=True, verbose_name='Description'),
        ),
        migrations.AddField(
            model_name='broadcast',
            name='preview_image',
            field=models.ImageField(blank=True, null=True, upload_to=homepage.uploadfiles.homepage_video_cover_upload_image_path, validators=[homepage.uploadfiles.video_image_restriction], verbose_name='Preview Image'),
        ),
        migrations.AddField(
            model_name='broadcast',
            name='streamSubtitle',
            field=models.CharField(blank=True, max_length=80, null=True, verbose_name='Stream Subtitle'),
        ),
        migrations.AddField(
            model_name='broadcast',
            name='streamTitle',
            field=models.CharField(default='tst', max_length=80, verbose_name='Stream Title'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='broadcast',
            name='subtitle',
            field=models.CharField(blank=True, max_length=80, null=True, verbose_name='Subtitle'),
        ),
    ]
