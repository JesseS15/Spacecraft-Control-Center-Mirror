# Generated by Django 4.1.2 on 2023-03-07 20:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('simapp', '0018_merge_20230305_1726'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sim',
            name='mission_script',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='simapp.mission'),
        ),
    ]