# Generated by Django 4.2.1 on 2024-01-16 10:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('activities', '0006_alter_event_day_alter_event_end_time_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='event',
            name='end_time',
        ),
        migrations.RemoveField(
            model_name='event',
            name='start_time',
        ),
        migrations.AlterField(
            model_name='event',
            name='end_date',
            field=models.DateTimeField(blank=True, null=True, verbose_name='End Date'),
        ),
        migrations.AlterField(
            model_name='event',
            name='start_date',
            field=models.DateTimeField(blank=True, null=True, verbose_name='Start Date'),
        ),
    ]
