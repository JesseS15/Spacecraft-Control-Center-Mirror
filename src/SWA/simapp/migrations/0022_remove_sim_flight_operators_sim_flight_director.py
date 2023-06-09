# Generated by Django 4.1.2 on 2023-03-08 17:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fo', '0009_flightoperator_class_list'),
        ('simapp', '0021_commandbufferitem_displaybufferitem_delete_acs_menu_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='sim',
            name='flight_operators',
        ),
        migrations.AddField(
            model_name='sim',
            name='flight_director',
            field=models.ManyToManyField(blank=True, default='', to='fo.flightoperator', verbose_name='Flight Director'),
        ),
    ]
