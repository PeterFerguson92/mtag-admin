# Generated by Django 4.2.1 on 2024-11-05 16:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('activities', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='day',
            field=models.CharField(choices=[('01-MONDAY', 'Monday'), ('02-TUESDAY', 'Tuesday'), ('03-WEDNESDAY', 'Wednesday'), ('04-THURSDAY', 'Thursday'), ('05-FRIDAY', 'Friday'), ('06-SATURDAY', 'Saturday'), ('07-SUNDAY', 'Sunday'), ('08-SUNDAY', 'Sunday 1st Service'), ('09-SUNDAY', 'Sunday 2nd Service')], max_length=5000, verbose_name='Day'),
        ),
        migrations.AlterField(
            model_name='event',
            name='description',
            field=models.TextField(blank=True, max_length=5000, null=True, verbose_name='Long Description'),
        ),
        migrations.AlterField(
            model_name='event',
            name='location',
            field=models.CharField(max_length=5000, verbose_name='Location'),
        ),
        migrations.AlterField(
            model_name='event',
            name='short_description',
            field=models.TextField(default='', max_length=5000, verbose_name='Short Description'),
        ),
        migrations.AlterField(
            model_name='event',
            name='title',
            field=models.CharField(max_length=5000, verbose_name='Title'),
        ),
    ]