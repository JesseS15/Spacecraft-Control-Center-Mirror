# Generated by Django 4.1.2 on 2023-03-05 20:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('simapp', '0015_alter_sim_flight_operators'),
    ]

    operations = [
        migrations.CreateModel(
            name='AllMissions',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('all_missions', models.ManyToManyField(blank=True, to='simapp.mission', verbose_name='All Missions')),
            ],
        ),
    ]