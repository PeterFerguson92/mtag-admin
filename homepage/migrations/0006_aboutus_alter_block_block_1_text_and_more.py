# Generated by Django 4.2.1 on 2024-01-19 17:43

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0005_block_homepage_blocks'),
    ]

    operations = [
        migrations.CreateModel(
            name='AboutUs',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('title', models.CharField(default='About Us', max_length=255, verbose_name='Title')),
                ('homepage_display_header', models.CharField(blank=True, max_length=30, null=True, verbose_name='Homepage Display Header')),
                ('homepage_display_title', models.CharField(max_length=30, verbose_name='Homepage Display Title')),
                ('homepage_display_text', models.TextField(max_length=60, verbose_name='Homepage Display Text')),
                ('homepage_display_info_1', models.CharField(blank=True, max_length=30, null=True, verbose_name='Homepage Display Info 1 Title')),
                ('homepage_display_info_1_text', models.TextField(blank=True, max_length=60, null=True, verbose_name='Homepage Display Info 1 Text')),
                ('homepage_display_info_2', models.CharField(blank=True, max_length=30, null=True, verbose_name='Homepage Display Info 2 Title')),
                ('homepage_display_info_2_text', models.TextField(blank=True, max_length=60, null=True, verbose_name='Homepage Display Info 2 Text')),
                ('section_display_header', models.CharField(blank=True, max_length=30, null=True, verbose_name='Section Display Header')),
                ('section_display_title', models.CharField(max_length=30, verbose_name='Section Display Title')),
                ('section_display_text', models.TextField(max_length=60, verbose_name='Section Display Text')),
                ('section_display_info_1', models.CharField(blank=True, max_length=30, null=True, verbose_name='Section Display Info 1 Title')),
                ('section_display_info_1_text', models.TextField(blank=True, max_length=60, null=True, verbose_name='Section Display Info 1 Text')),
                ('section_display_info_2', models.CharField(blank=True, max_length=30, null=True, verbose_name='Section Display Info 2 Title')),
                ('section_display_info_2_text', models.TextField(blank=True, max_length=60, null=True, verbose_name='Section Display Info 2 Text')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created at')),
            ],
            options={
                'verbose_name': 'About Us',
                'verbose_name_plural': 'About Us',
                'ordering': ('title', 'created_at'),
            },
        ),
        migrations.AlterField(
            model_name='block',
            name='block_1_text',
            field=models.TextField(max_length=60, verbose_name='Block 1 Text'),
        ),
        migrations.AlterField(
            model_name='block',
            name='block_1_title',
            field=models.CharField(max_length=30, verbose_name='Block 1 Title'),
        ),
        migrations.AlterField(
            model_name='block',
            name='block_2_text',
            field=models.TextField(max_length=60, verbose_name='Block 2 Text'),
        ),
        migrations.AlterField(
            model_name='block',
            name='block_2_title',
            field=models.CharField(max_length=30, verbose_name='Block 2 Title'),
        ),
        migrations.AlterField(
            model_name='block',
            name='block_3_text',
            field=models.TextField(max_length=60, verbose_name='Block 3 Text'),
        ),
        migrations.AlterField(
            model_name='block',
            name='block_3_title',
            field=models.CharField(max_length=30, verbose_name='Block 3 Title'),
        ),
        migrations.AddField(
            model_name='homepage',
            name='aboutUs',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='homepage.aboutus'),
        ),
    ]
