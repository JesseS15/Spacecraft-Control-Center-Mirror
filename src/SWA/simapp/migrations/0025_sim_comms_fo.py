# Generated by Django 4.1.2 on 2023-03-08 20:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fo', '0009_flightoperator_class_list'),
        ('simapp', '0024_alter_sim_flight_director'),
    ]

    operations = [
        migrations.AddField(
            model_name='sim',
            name='COMMS_fo',
            field=models.ManyToManyField(blank=True, default='', related_name='comms_fo', to='fo.flightoperator', verbose_name='Comms Flight Operator'),
        ),
    ]
