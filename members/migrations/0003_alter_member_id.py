# Generated by Django 4.2.1 on 2024-02-03 20:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0002_alter_transaction_service_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='member',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
