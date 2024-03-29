# Generated by Django 4.2.1 on 2024-02-04 19:44

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('servicemanagement', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Attendance',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('date', models.DateField(verbose_name='Date')),
                ('number_of_mens', models.IntegerField(blank=True, null=True, verbose_name="Number of Men's")),
                ('number_of_women', models.IntegerField(blank=True, null=True, verbose_name="Number of Women's")),
                ('number_of_youth', models.IntegerField(blank=True, null=True, verbose_name="Number of Youth's")),
                ('number_of_children', models.IntegerField(blank=True, null=True, verbose_name="Number of Children's")),
                ('total', models.IntegerField(blank=True, null=True, verbose_name='Total')),
                ('service_type', models.CharField(blank=True, choices=[('TUESDAY BIBLE STUDIES', 'Tuesday Bible studies'), ('FRIDAY_PRAYER_MEETING', 'Friday Prayer Meeting'), ('1_SUNDAY_SERVICE', 'Sunday 1st Service'), ('2_SUNDAY_SERVICE', 'Sunday 2nd Service')], max_length=255, null=True, verbose_name='Service Type')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created at')),
            ],
            options={
                'verbose_name_plural': 'Attendance',
                'ordering': ('date', 'created_at'),
            },
        ),
    ]
