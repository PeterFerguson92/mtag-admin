# Generated by Django 4.2.1 on 2024-03-27 17:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('activities', '0003_alter_socialevent_options'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='socialevent',
            name='gallery_image_path_3',
        ),
        migrations.RemoveField(
            model_name='socialevent',
            name='gallery_image_path_4',
        ),
        migrations.AddField(
            model_name='socialevent',
            name='end_date',
            field=models.DateField(blank=True, null=True, verbose_name='End Date'),
        ),
        migrations.AddField(
            model_name='socialevent',
            name='start_date',
            field=models.DateField(blank=True, null=True, verbose_name='Start Date'),
        ),
    ]
