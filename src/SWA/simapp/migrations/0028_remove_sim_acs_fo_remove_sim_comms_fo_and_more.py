# Generated by Django 4.1.2 on 2023-03-23 03:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('simapp', '0027_alter_sim_flight_director'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='sim',
            name='ACS_fo',
        ),
        migrations.RemoveField(
            model_name='sim',
            name='COMMS_fo',
        ),
        migrations.RemoveField(
            model_name='sim',
            name='EPS_fo',
        ),
        migrations.RemoveField(
            model_name='sim',
            name='TCS_fo',
        ),
        migrations.RemoveField(
            model_name='sim',
            name='flight_director',
        ),
    ]
