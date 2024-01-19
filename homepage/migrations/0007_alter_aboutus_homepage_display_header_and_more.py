# Generated by Django 4.2.1 on 2024-01-19 17:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0006_aboutus_alter_block_block_1_text_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aboutus',
            name='homepage_display_header',
            field=models.CharField(blank=True, max_length=80, null=True, verbose_name='Homepage Display Header'),
        ),
        migrations.AlterField(
            model_name='aboutus',
            name='homepage_display_info_1',
            field=models.CharField(blank=True, max_length=80, null=True, verbose_name='Homepage Display Info 1 Title'),
        ),
        migrations.AlterField(
            model_name='aboutus',
            name='homepage_display_info_1_text',
            field=models.TextField(blank=True, max_length=120, null=True, verbose_name='Homepage Display Info 1 Text'),
        ),
        migrations.AlterField(
            model_name='aboutus',
            name='homepage_display_info_2',
            field=models.CharField(blank=True, max_length=80, null=True, verbose_name='Homepage Display Info 2 Title'),
        ),
        migrations.AlterField(
            model_name='aboutus',
            name='homepage_display_info_2_text',
            field=models.TextField(blank=True, max_length=120, null=True, verbose_name='Homepage Display Info 2 Text'),
        ),
        migrations.AlterField(
            model_name='aboutus',
            name='homepage_display_text',
            field=models.TextField(max_length=120, verbose_name='Homepage Display Text'),
        ),
        migrations.AlterField(
            model_name='aboutus',
            name='homepage_display_title',
            field=models.CharField(max_length=80, verbose_name='Homepage Display Title'),
        ),
        migrations.AlterField(
            model_name='aboutus',
            name='section_display_header',
            field=models.CharField(blank=True, max_length=80, null=True, verbose_name='Section Display Header'),
        ),
        migrations.AlterField(
            model_name='aboutus',
            name='section_display_info_1',
            field=models.CharField(blank=True, max_length=80, null=True, verbose_name='Section Display Info 1 Title'),
        ),
        migrations.AlterField(
            model_name='aboutus',
            name='section_display_info_1_text',
            field=models.TextField(blank=True, max_length=120, null=True, verbose_name='Section Display Info 1 Text'),
        ),
        migrations.AlterField(
            model_name='aboutus',
            name='section_display_info_2',
            field=models.CharField(blank=True, max_length=80, null=True, verbose_name='Section Display Info 2 Title'),
        ),
        migrations.AlterField(
            model_name='aboutus',
            name='section_display_info_2_text',
            field=models.TextField(blank=True, max_length=120, null=True, verbose_name='Section Display Info 2 Text'),
        ),
        migrations.AlterField(
            model_name='aboutus',
            name='section_display_text',
            field=models.TextField(max_length=120, verbose_name='Section Display Text'),
        ),
        migrations.AlterField(
            model_name='aboutus',
            name='section_display_title',
            field=models.CharField(max_length=80, verbose_name='Section Display Title'),
        ),
        migrations.AlterField(
            model_name='block',
            name='block_1_text',
            field=models.TextField(max_length=120, verbose_name='Block 1 Text'),
        ),
        migrations.AlterField(
            model_name='block',
            name='block_1_title',
            field=models.CharField(max_length=80, verbose_name='Block 1 Title'),
        ),
        migrations.AlterField(
            model_name='block',
            name='block_2_text',
            field=models.TextField(max_length=120, verbose_name='Block 2 Text'),
        ),
        migrations.AlterField(
            model_name='block',
            name='block_2_title',
            field=models.CharField(max_length=80, verbose_name='Block 2 Title'),
        ),
        migrations.AlterField(
            model_name='block',
            name='block_3_text',
            field=models.TextField(max_length=120, verbose_name='Block 3 Text'),
        ),
        migrations.AlterField(
            model_name='block',
            name='block_3_title',
            field=models.CharField(max_length=80, verbose_name='Block 3 Title'),
        ),
    ]
