# Generated by Django 4.1.2 on 2023-02-16 21:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('simapp', '0001_initial'),
        ('fo', '0005_post_like'),
    ]

    operations = [
        migrations.AlterField(
            model_name='flightoperator',
            name='sim_list',
            field=models.ManyToManyField(to='simapp.sim', verbose_name='Sim'),
        ),
    ]
