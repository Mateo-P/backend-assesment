# Generated by Django 4.0 on 2022-01-11 20:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('itineraries', '0003_leg_duration_mins'),
    ]

    operations = [
        migrations.AlterField(
            model_name='leg',
            name='arrival_time',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='leg',
            name='departure_time',
            field=models.DateTimeField(),
        ),
    ]
