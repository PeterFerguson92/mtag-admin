# Generated by Django 4.2.1 on 2024-01-23 10:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0003_alter_serviceplanning_bible_reading_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='serviceplanning',
            name='bible_reading_end_time',
            field=models.TimeField(blank=True, null=True, verbose_name='Bible Reading End Time'),
        ),
        migrations.AddField(
            model_name='serviceplanning',
            name='bible_reading_start_time',
            field=models.TimeField(blank=True, null=True, verbose_name='Bible Reading Start Time'),
        ),
        migrations.AddField(
            model_name='serviceplanning',
            name='expected_bible_reading_end_time',
            field=models.TimeField(blank=True, null=True, verbose_name='Expected Bible Reading End Time'),
        ),
        migrations.AddField(
            model_name='serviceplanning',
            name='expected_bible_reading_start_time',
            field=models.TimeField(blank=True, null=True, verbose_name='Expected Bible Reading Start Time'),
        ),
        migrations.AddField(
            model_name='serviceplanning',
            name='expected_mc_end_time',
            field=models.TimeField(blank=True, null=True, verbose_name='Expected MC End Time'),
        ),
        migrations.AddField(
            model_name='serviceplanning',
            name='expected_mc_start_time',
            field=models.TimeField(blank=True, null=True, verbose_name='Expected MC Start Time'),
        ),
        migrations.AddField(
            model_name='serviceplanning',
            name='expected_mtag_news_end_time',
            field=models.TimeField(blank=True, null=True, verbose_name='Expected MTAG news End Time'),
        ),
        migrations.AddField(
            model_name='serviceplanning',
            name='expected_mtag_news_start_time',
            field=models.TimeField(blank=True, null=True, verbose_name='Expected MTAG news Start Time'),
        ),
        migrations.AddField(
            model_name='serviceplanning',
            name='expected_offering_ministration_end_time',
            field=models.TimeField(blank=True, null=True, verbose_name='Expected Offering & Ministration End Time'),
        ),
        migrations.AddField(
            model_name='serviceplanning',
            name='expected_offering_ministration_start_time',
            field=models.TimeField(blank=True, null=True, verbose_name='Expected Offering & Ministration Start Time'),
        ),
        migrations.AddField(
            model_name='serviceplanning',
            name='expected_sermon_end_time',
            field=models.TimeField(blank=True, null=True, verbose_name='Expected Sermon End Time'),
        ),
        migrations.AddField(
            model_name='serviceplanning',
            name='expected_sermon_start_time',
            field=models.TimeField(blank=True, null=True, verbose_name='Expected Sermon Start Time'),
        ),
        migrations.AddField(
            model_name='serviceplanning',
            name='expected_worship_praise_end_time',
            field=models.TimeField(blank=True, null=True, verbose_name='Expected Worship and Praise End Time'),
        ),
        migrations.AddField(
            model_name='serviceplanning',
            name='expected_worship_praise_start_time',
            field=models.TimeField(blank=True, null=True, verbose_name='Expected Worship and Praise Time'),
        ),
        migrations.AddField(
            model_name='serviceplanning',
            name='mc_end_time',
            field=models.TimeField(blank=True, null=True, verbose_name='MC End Time'),
        ),
        migrations.AddField(
            model_name='serviceplanning',
            name='mc_start_time',
            field=models.TimeField(blank=True, null=True, verbose_name='MC Start Time'),
        ),
        migrations.AddField(
            model_name='serviceplanning',
            name='mtag_news_end_time',
            field=models.TimeField(blank=True, null=True, verbose_name='MTAG news End Time'),
        ),
        migrations.AddField(
            model_name='serviceplanning',
            name='mtag_news_start_time',
            field=models.TimeField(blank=True, null=True, verbose_name='MTAG news Start Time'),
        ),
        migrations.AddField(
            model_name='serviceplanning',
            name='offering_ministration_end_time',
            field=models.TimeField(blank=True, null=True, verbose_name='Offering & Ministration End Time'),
        ),
        migrations.AddField(
            model_name='serviceplanning',
            name='offering_ministration_start_time',
            field=models.TimeField(blank=True, null=True, verbose_name='Offering & Ministration Start Time'),
        ),
        migrations.AddField(
            model_name='serviceplanning',
            name='sermon_end_time',
            field=models.TimeField(blank=True, null=True, verbose_name='Sermon End Time'),
        ),
        migrations.AddField(
            model_name='serviceplanning',
            name='sermon_start_time',
            field=models.TimeField(blank=True, null=True, verbose_name='Sermon Start Time'),
        ),
        migrations.AddField(
            model_name='serviceplanning',
            name='worship_praise_end_time',
            field=models.TimeField(blank=True, null=True, verbose_name='Worship and Praise End Time'),
        ),
        migrations.AddField(
            model_name='serviceplanning',
            name='worship_praise_start_time',
            field=models.TimeField(blank=True, null=True, verbose_name='Worship and Praise Start Time'),
        ),
    ]