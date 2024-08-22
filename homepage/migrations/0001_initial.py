# Generated by Django 4.2.1 on 2024-08-22 21:52

from django.db import migrations, models
import django.db.models.deletion
import django_resized.forms
import homepage.uploadfiles
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AboutUs',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('title', models.CharField(default='About Us', max_length=255, verbose_name='Title')),
                ('homepage_display_header', models.CharField(blank=True, max_length=80, null=True, verbose_name='Homepage Display Header')),
                ('homepage_display_title', models.CharField(max_length=80, verbose_name='Homepage Display Title')),
                ('homepage_display_text', models.TextField(max_length=180, verbose_name='Homepage Display Text')),
                ('homepage_display_info_1', models.CharField(blank=True, max_length=80, null=True, verbose_name='Homepage Display Info 1 Title')),
                ('homepage_display_info_1_text', models.TextField(blank=True, max_length=180, null=True, verbose_name='Homepage Display Info 1 Text')),
                ('homepage_display_info_2', models.CharField(blank=True, max_length=80, null=True, verbose_name='Homepage Display Info 2 Title')),
                ('homepage_display_info_2_text', models.TextField(blank=True, max_length=180, null=True, verbose_name='Homepage Display Info 2 Text')),
                ('homepage_image', django_resized.forms.ResizedImageField(blank=True, crop=None, force_format=None, keep_meta=True, null=True, quality=-1, scale=None, size=[371, 421], upload_to=homepage.uploadfiles.homepage_about_us_cover_upload_image_path, verbose_name='Homepage Image')),
                ('section_display_header', models.CharField(blank=True, max_length=80, null=True, verbose_name='Section Display Header')),
                ('section_display_title', models.CharField(max_length=80, verbose_name='Section Display Title')),
                ('section_display_text', models.TextField(max_length=180, verbose_name='Section Display Text')),
                ('section_display_info_1', models.CharField(blank=True, max_length=80, null=True, verbose_name='Section Display Info 1 Title')),
                ('section_display_info_1_text', models.TextField(blank=True, max_length=255, null=True, verbose_name='Section Display Info 1 Text')),
                ('section_display_info_2', models.CharField(blank=True, max_length=80, null=True, verbose_name='Section Display Info 2 Title')),
                ('section_display_info_2_text', models.TextField(blank=True, max_length=255, null=True, verbose_name='Section Display Info 2 Text')),
                ('image_1', django_resized.forms.ResizedImageField(blank=True, crop=None, force_format=None, keep_meta=True, null=True, quality=-1, scale=None, size=[271, 301], upload_to=homepage.uploadfiles.homepage_about_us_cover_upload_image_path, verbose_name='Image 1')),
                ('image_2', django_resized.forms.ResizedImageField(blank=True, crop=None, force_format=None, keep_meta=True, null=True, quality=-1, scale=None, size=[271, 301], upload_to=homepage.uploadfiles.homepage_about_us_cover_upload_image_path, verbose_name='Image 2')),
                ('image_3', django_resized.forms.ResizedImageField(blank=True, crop=None, force_format=None, keep_meta=True, null=True, quality=-1, scale=None, size=[271, 301], upload_to=homepage.uploadfiles.homepage_about_us_cover_upload_image_path, verbose_name='Image 3')),
                ('image_4', django_resized.forms.ResizedImageField(blank=True, crop=None, force_format=None, keep_meta=True, null=True, quality=-1, scale=None, size=[271, 301], upload_to=homepage.uploadfiles.homepage_about_us_cover_upload_image_path, verbose_name='Image 4')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created at')),
            ],
            options={
                'verbose_name': 'About Us',
                'verbose_name_plural': 'About Us',
                'ordering': ('title', 'created_at'),
            },
        ),
        migrations.CreateModel(
            name='Banner',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=255, verbose_name='Title')),
                ('text', models.TextField(blank=True, max_length=1024, null=True, verbose_name='Text')),
                ('image', django_resized.forms.ResizedImageField(blank=True, crop=None, force_format=None, keep_meta=True, null=True, quality=-1, scale=None, size=[203, 223], upload_to=homepage.uploadfiles.homepage_banner_upload_image_path, verbose_name='Image')),
                ('image_position', models.CharField(blank=True, choices=[('left', 'left'), ('right', 'right')], max_length=255, null=True, verbose_name='position')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created at')),
            ],
            options={
                'verbose_name': 'Banner',
                'verbose_name_plural': 'Banners',
                'ordering': ('title', 'created_at'),
            },
        ),
        migrations.CreateModel(
            name='Block',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('title', models.CharField(default='Block Section', max_length=255, verbose_name='Title')),
                ('block_1_title', models.CharField(max_length=80, verbose_name='Block 1 Title')),
                ('block_1_text', models.TextField(max_length=120, verbose_name='Block 1 Text')),
                ('block_2_title', models.CharField(max_length=80, verbose_name='Block 2 Title')),
                ('block_2_text', models.TextField(max_length=120, verbose_name='Block 2 Text')),
                ('block_3_title', models.CharField(max_length=80, verbose_name='Block 3 Title')),
                ('block_3_text', models.TextField(max_length=120, verbose_name='Block 3 Text')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created at')),
            ],
            options={
                'verbose_name': 'Block',
                'verbose_name_plural': 'Blocks',
                'ordering': ('title', 'created_at'),
            },
        ),
        migrations.CreateModel(
            name='Broadcast',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=80, verbose_name='Title')),
                ('subtitle', models.CharField(blank=True, max_length=80, null=True, verbose_name='Subtitle')),
                ('preview_image', django_resized.forms.ResizedImageField(blank=True, crop=None, force_format=None, keep_meta=True, null=True, quality=-1, scale=None, size=[561, 430], upload_to=homepage.uploadfiles.homepage_video_cover_upload_image_path, verbose_name='Preview Image')),
                ('link', models.CharField(max_length=255, verbose_name='Link')),
                ('stream_title', models.CharField(max_length=80, verbose_name='Stream Title')),
                ('stream_subtitle', models.CharField(blank=True, max_length=80, null=True, verbose_name='Stream Subtitle')),
                ('stream_description', models.TextField(blank=True, max_length=230, null=True, verbose_name='Description')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created at')),
            ],
            options={
                'verbose_name': 'Broadcast',
                'verbose_name_plural': 'Broadcast',
                'ordering': ('title', 'created_at'),
            },
        ),
        migrations.CreateModel(
            name='Details',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('title', models.CharField(default='Church Details', max_length=255, verbose_name='Title')),
                ('info_text_1', models.CharField(blank=True, max_length=80, null=True, verbose_name='Info Text 1')),
                ('info_content_1', models.CharField(blank=True, max_length=80, null=True, verbose_name='Info Content 1')),
                ('info_text_2', models.CharField(blank=True, max_length=80, null=True, verbose_name='Info Text 2')),
                ('info_content_2', models.CharField(blank=True, max_length=80, null=True, verbose_name='Info Content 2')),
                ('address', models.CharField(blank=True, max_length=180, null=True, verbose_name='Address')),
                ('description', models.TextField(blank=True, max_length=280, null=True, verbose_name='Description')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created at')),
            ],
            options={
                'verbose_name': 'Details',
                'verbose_name_plural': 'Details',
                'ordering': ('title', 'created_at'),
            },
        ),
        migrations.CreateModel(
            name='Leader',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('fullName', models.CharField(max_length=300, verbose_name='Full Name')),
                ('role', models.CharField(max_length=300, verbose_name='Role')),
                ('description', models.TextField(max_length=700, verbose_name='Description')),
                ('phone', models.CharField(max_length=100, verbose_name='Phone Number')),
                ('address', models.CharField(blank=True, max_length=200, null=True, verbose_name='Address')),
                ('image', django_resized.forms.ResizedImageField(blank=True, crop=None, force_format=None, keep_meta=True, null=True, quality=-1, scale=None, size=[466, 494], upload_to=homepage.uploadfiles.homepage_leader_cover_upload_image_path, verbose_name='Image')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created at')),
            ],
            options={
                'verbose_name': 'Leader',
                'verbose_name_plural': 'Leaders',
                'ordering': ('fullName', 'created_at'),
            },
        ),
        migrations.CreateModel(
            name='Media',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('title', models.CharField(default='Media', max_length=80, verbose_name='Title')),
                ('videos_header', models.CharField(blank=True, max_length=80, null=True, verbose_name='Video Section Header')),
                ('videos_title', models.CharField(blank=True, max_length=80, null=True, verbose_name='Video Section Title')),
                ('video_id', models.CharField(max_length=80, verbose_name='Video id')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created at')),
            ],
            options={
                'verbose_name': 'Media',
                'verbose_name_plural': 'Media',
                'ordering': ('title', 'created_at'),
            },
        ),
        migrations.CreateModel(
            name='SocialMedia',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('title', models.CharField(default='Social Media Links', max_length=255, verbose_name='Title')),
                ('facebook_link', models.CharField(max_length=255, verbose_name='Facebook Link')),
                ('tiktok_link', models.CharField(max_length=255, verbose_name='Tik Tok Link')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created at')),
            ],
            options={
                'verbose_name': 'Social Media',
                'verbose_name_plural': 'Social Media',
                'ordering': ('title', 'created_at'),
            },
        ),
        migrations.CreateModel(
            name='Video',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=80, verbose_name='Title')),
                ('description', models.TextField(blank=True, max_length=180, null=True, verbose_name='Description')),
                ('date', models.DateField(blank=True, null=True, verbose_name='Date')),
                ('image', django_resized.forms.ResizedImageField(blank=True, crop=None, force_format=None, keep_meta=True, null=True, quality=-1, scale=None, size=[561, 430], upload_to=homepage.uploadfiles.homepage_video_cover_upload_image_path, verbose_name='Image')),
                ('url', models.CharField(max_length=255, verbose_name='Url')),
                ('featured', models.BooleanField(default=False, verbose_name='Featured')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created at')),
            ],
            options={
                'verbose_name': 'Video',
                'verbose_name_plural': 'Video',
                'ordering': ('title', 'created_at'),
            },
        ),
        migrations.CreateModel(
            name='LeadershipBoard',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('title', models.CharField(default='Leadership Board', max_length=80, verbose_name='Title')),
                ('header', models.CharField(blank=True, max_length=80, null=True, verbose_name='Section Header')),
                ('section_title', models.CharField(blank=True, max_length=80, null=True, verbose_name='Section Title')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created at')),
                ('leaders', models.ManyToManyField(to='homepage.leader')),
            ],
            options={
                'verbose_name': 'Leadership Board',
                'verbose_name_plural': 'Leadership Board',
                'ordering': ('title', 'created_at'),
            },
        ),
        migrations.CreateModel(
            name='Homepage',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('title', models.CharField(default='Homepage', max_length=255, verbose_name='Title')),
                ('banner_background_image', django_resized.forms.ResizedImageField(blank=True, crop=None, force_format=None, keep_meta=True, null=True, quality=-1, scale=None, size=[1921, 905], upload_to=homepage.uploadfiles.homepage_background_upload_image_path, verbose_name='Banner Background Image')),
                ('leadership_board_background_image', django_resized.forms.ResizedImageField(blank=True, crop=None, force_format=None, keep_meta=True, null=True, quality=-1, scale=None, size=[1921, 905], upload_to=homepage.uploadfiles.homepage_background_upload_image_path, verbose_name='Leadership Board Background Image')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created at')),
                ('aboutUs', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='homepage.aboutus')),
                ('banners', models.ManyToManyField(blank=True, null=True, to='homepage.banner')),
                ('blocks', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='homepage.block')),
                ('details', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='homepage.details')),
                ('leadershipBoard', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='homepage.leadershipboard')),
                ('media', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='homepage.media')),
            ],
            options={
                'verbose_name': 'Homepage',
                'verbose_name_plural': 'Homepage',
                'ordering': ('created_at',),
            },
        ),
    ]
