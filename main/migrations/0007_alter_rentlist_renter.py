# Generated by Django 5.0.4 on 2024-04-29 23:07

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_rentlist'),
        ('users', '0012_alter_clients_fullname'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rentlist',
            name='renter',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='users.profile'),
        ),
    ]
