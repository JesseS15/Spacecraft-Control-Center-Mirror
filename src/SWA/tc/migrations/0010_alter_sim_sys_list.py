# Generated by Django 4.1.2 on 2022-12-02 20:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tc', '0009_remove_sim_button_value'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sim',
            name='sys_list',
            field=models.ManyToManyField(to='tc.simsys'),
        ),
    ]