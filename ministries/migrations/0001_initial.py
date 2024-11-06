# Generated by Django 4.2.1 on 2024-09-26 19:42

from django.db import migrations, models
import django_resized.forms
import ministries.uploadfiles
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Ministry',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255, verbose_name='Name')),
                ('short_description', models.TextField(default='', max_length=400, verbose_name='Short Description')),
                ('description', models.TextField(blank=True, max_length=1024, null=True, verbose_name='Long Description')),
                ('cover_image_path', django_resized.forms.ResizedImageField(crop=None, force_format=None, keep_meta=True, quality=-1, scale=None, size=[421, 371], upload_to=ministries.uploadfiles.ministries_upload_image_path, verbose_name='Cover image')),
                ('gallery_image_path_1', django_resized.forms.ResizedImageField(blank=True, crop=None, force_format=None, keep_meta=True, null=True, quality=-1, scale=None, size=[370, 370], upload_to=ministries.uploadfiles.ministries_upload_image_path, verbose_name='Gallery image 1')),
                ('gallery_image_path_2', django_resized.forms.ResizedImageField(blank=True, crop=None, force_format=None, keep_meta=True, null=True, quality=-1, scale=None, size=[370, 370], upload_to=ministries.uploadfiles.ministries_upload_image_path, verbose_name='Gallery image 2')),
                ('gallery_image_path_3', django_resized.forms.ResizedImageField(blank=True, crop=None, force_format=None, keep_meta=True, null=True, quality=-1, scale=None, size=[370, 370], upload_to=ministries.uploadfiles.ministries_upload_image_path, verbose_name='Gallery image 3')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created at')),
            ],
            options={
                'verbose_name_plural': 'Ministries',
                'ordering': ('name', 'created_at'),
            },
        ),
    ]
