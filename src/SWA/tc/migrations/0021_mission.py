# Generated by Django 4.1.2 on 2023-02-24 04:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tc', '0020_class_code_alter_class_sims_delete_sim_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Mission',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mission_name', models.CharField(default='', max_length=15)),
            ],
            options={
                'verbose_name_plural': 'Missions',
            },
        ),
    ]