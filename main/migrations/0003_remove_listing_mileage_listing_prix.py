# Generated by Django 5.0.4 on 2024-04-29 13:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_rename_transmisson_listing_transmission_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='listing',
            name='mileage',
        ),
        migrations.AddField(
            model_name='listing',
            name='prix',
            field=models.IntegerField(default=0),
        ),
    ]
