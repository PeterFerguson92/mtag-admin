# Generated by Django 4.2.1 on 2025-02-18 21:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('servicemanagement', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='attendance',
            name='service_type',
            field=models.CharField(choices=[('01-SERVICE', '1st Service'), ('02-SERVICE', '2nd Service'), ('03-SERVICE', '3rd Service'), ('04-SERVICE', 'Joint Service')], default='1st Service', max_length=255, verbose_name='Service Type'),
        ),
        migrations.AlterField(
            model_name='serviceplanning',
            name='service_type',
            field=models.CharField(choices=[('01-SERVICE', '1st Service'), ('02-SERVICE', '2nd Service'), ('03-SERVICE', '3rd Service'), ('04-SERVICE', 'Joint Service')], max_length=255, verbose_name='Service Type'),
        ),
    ]
