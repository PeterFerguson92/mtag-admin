# Generated by Django 4.2.1 on 2024-01-19 12:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='banner',
            name='image_position',
            field=models.CharField(blank=True, choices=[('left', 'left'), ('right', 'right')], max_length=255, null=True, verbose_name='position'),
        ),
    ]
