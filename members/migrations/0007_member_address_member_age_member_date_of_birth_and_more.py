# Generated by Django 4.2.1 on 2024-01-17 11:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0006_alter_member_member_type_alter_member_sex'),
    ]

    operations = [
        migrations.AddField(
            model_name='member',
            name='address',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Address'),
        ),
        migrations.AddField(
            model_name='member',
            name='age',
            field=models.IntegerField(blank=True, max_length=255, null=True, verbose_name='Age'),
        ),
        migrations.AddField(
            model_name='member',
            name='date_of_birth',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Date Of Birth'),
        ),
        migrations.AddField(
            model_name='member',
            name='postcode',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Postcode'),
        ),
        migrations.AddField(
            model_name='member',
            name='test',
            field=models.DurationField(blank=True, max_length=255, null=True, verbose_name='Membership start'),
        ),
        migrations.AlterField(
            model_name='member',
            name='member_type',
            field=models.CharField(choices=[('FULL MEMBER', 'Full Member'), ('VISITOR', 'Visitor')], default='Full Member', max_length=255, verbose_name='Member type'),
        ),
        migrations.AlterField(
            model_name='member',
            name='sex',
            field=models.CharField(choices=[('Female', 'Female'), ('Male', 'Male')], max_length=50),
        ),
    ]
