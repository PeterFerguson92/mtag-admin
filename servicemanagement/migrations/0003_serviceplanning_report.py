# Generated by Django 4.2.1 on 2024-12-04 18:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('servicemanagement', '0002_alter_absence_reason'),
    ]

    operations = [
        migrations.AddField(
            model_name='serviceplanning',
            name='report',
            field=models.TextField(blank=True, null=True, verbose_name='Report'),
        ),
    ]
