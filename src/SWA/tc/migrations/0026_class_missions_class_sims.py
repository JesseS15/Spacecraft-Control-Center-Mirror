# Generated by Django 4.1.2 on 2023-03-04 20:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('simapp', '0014_remove_sim_acs_subsys'),
        ('tc', '0025_remove_class_missions_remove_class_sims'),
    ]

    operations = [
        migrations.AddField(
            model_name='class',
            name='missions',
            field=models.ManyToManyField(to='simapp.mission', verbose_name='Mission'),
        ),
        migrations.AddField(
            model_name='class',
            name='sims',
            field=models.ManyToManyField(blank=True, to='simapp.sim', verbose_name='Sim'),
        ),
    ]
