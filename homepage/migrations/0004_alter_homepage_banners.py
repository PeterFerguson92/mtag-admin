# Generated by Django 4.2.1 on 2024-02-16 21:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0003_alter_homepage_aboutus_alter_homepage_blocks_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='homepage',
            name='banners',
            field=models.ManyToManyField(blank=True, null=True, to='homepage.banner'),
        ),
    ]
