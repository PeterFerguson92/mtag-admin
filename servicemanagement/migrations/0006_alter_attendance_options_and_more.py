# Generated by Django 4.2.1 on 2024-02-06 10:49

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('servicemanagement', '0005_member_last_seen'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='attendance',
            options={'ordering': ('date', 'created_at'), 'verbose_name': 'Service Attendance', 'verbose_name_plural': 'Service Attendance'},
        ),
        migrations.RemoveField(
            model_name='attendance',
            name='service_type',
        ),
        migrations.CreateModel(
            name='Absence',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('contact_phone_number', models.CharField(max_length=255, verbose_name='Contact Phone Number')),
                ('last_seen', models.DateField(verbose_name='Last seen')),
                ('reason', models.TextField(blank=True, max_length=255, verbose_name='Reason')),
                ('contacted', models.BooleanField(default=False, verbose_name='Contacted')),
                ('contacted_date', models.DateField(blank=True, null=True, verbose_name='Last seen')),
                ('person_of_contact', models.CharField(blank=True, max_length=255, null=True, verbose_name='Person of contact')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created at')),
                ('member', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='absent_member', to='servicemanagement.member')),
            ],
            options={
                'verbose_name_plural': 'Member Absence',
                'ordering': ('member', 'created_at'),
            },
        ),
    ]
