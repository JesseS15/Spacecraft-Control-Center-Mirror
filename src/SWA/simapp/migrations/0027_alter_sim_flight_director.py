# Generated by Django 4.1.2 on 2023-03-22 17:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fo', '0009_flightoperator_class_list'),
        ('simapp', '0026_sim_acs_fo_sim_eps_fo_sim_tcs_fo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sim',
            name='flight_director',
            field=models.ManyToManyField(blank=True, default='fd_fo', to='fo.flightoperator', verbose_name='Flight Director'),
        ),
    ]
