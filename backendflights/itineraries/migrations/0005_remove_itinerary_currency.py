# Generated by Django 4.0 on 2022-01-11 22:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('itineraries', '0004_alter_leg_arrival_time_alter_leg_departure_time'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='itinerary',
            name='currency',
        ),
    ]
