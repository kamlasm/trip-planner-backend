# Generated by Django 5.0.7 on 2024-07-14 10:06

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trips', '0004_remove_trip_hotels'),
    ]

    operations = [
        migrations.AlterField(
            model_name='trip',
            name='activities',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(blank=True, max_length=500), default=list, size=None),
        ),
    ]
