# Generated by Django 4.2.1 on 2024-02-06 18:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('servicemanagement', '0013_alter_absence_source'),
    ]

    operations = [
        migrations.AlterField(
            model_name='absence',
            name='source',
            field=models.CharField(blank=True, choices=[('IMPORT', 'Import'), ('MANUAL', 'Manual')], default='IMPORT', max_length=255, null=True, verbose_name='Source'),
        ),
    ]
