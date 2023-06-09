# Generated by Django 4.1.6 on 2023-05-05 23:04

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('simapp', '0044_alter_mission_final_pitch_alter_mission_final_roll_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mission',
            name='final_pitch',
            field=models.IntegerField(blank=True, default=23, validators=[django.core.validators.MinValueValidator(-90), django.core.validators.MaxValueValidator(90)]),
        ),
        migrations.AlterField(
            model_name='mission',
            name='final_roll',
            field=models.IntegerField(blank=True, default=6, validators=[django.core.validators.MinValueValidator(-180), django.core.validators.MaxValueValidator(180)]),
        ),
        migrations.AlterField(
            model_name='mission',
            name='final_yaw',
            field=models.IntegerField(blank=True, default=92, validators=[django.core.validators.MinValueValidator(-180), django.core.validators.MaxValueValidator(180)]),
        ),
    ]
