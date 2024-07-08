# Generated by Django 5.0.6 on 2024-07-08 17:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trips', '0009_alter_trip_flight_back_time_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='trip',
            name='budget',
            field=models.FloatField(blank=True, default=0),
        ),
        migrations.AlterField(
            model_name='trip',
            name='flight_back_time',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='trip',
            name='flight_out_time',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='trip',
            name='flights_cost',
            field=models.FloatField(blank=True, default=0),
        ),
        migrations.AlterField(
            model_name='trip',
            name='hotels_cost',
            field=models.FloatField(blank=True, default=0),
        ),
    ]
