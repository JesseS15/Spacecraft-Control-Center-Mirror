# Generated by Django 4.1.6 on 2023-04-19 23:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('simapp', '0040_alter_mission_final_pitch_alter_mission_final_roll_and_more'),
        ('tc', '0033_remove_class_sims_class_missions'),
    ]

    operations = [
        migrations.AddField(
            model_name='class',
            name='sims',
            field=models.ManyToManyField(blank=True, to='simapp.sim', verbose_name='Sim'),
        ),
    ]
