# Generated by Django 4.1.2 on 2023-03-04 20:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('simapp', '0011_remove_sim_acs_subsys_remove_sim_command_buffer_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='subsystem',
            name='subsys_menu',
        ),
    ]
