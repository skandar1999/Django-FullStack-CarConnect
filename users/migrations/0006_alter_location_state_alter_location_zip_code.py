# Generated by Django 5.0.4 on 2024-04-25 15:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_alter_profile_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='location',
            name='state',
            field=models.CharField(blank=True, max_length=128),
        ),
        migrations.AlterField(
            model_name='location',
            name='zip_code',
            field=models.CharField(blank=True, max_length=128),
        ),
    ]
