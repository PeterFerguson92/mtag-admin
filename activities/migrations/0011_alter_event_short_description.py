# Generated by Django 4.2.1 on 2024-01-18 12:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('activities', '0010_event_short_description_alter_event_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='short_description',
            field=models.CharField(default='', max_length=1024, verbose_name='Short Description'),
        ),
    ]
