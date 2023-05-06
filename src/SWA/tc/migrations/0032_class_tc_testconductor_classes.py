# Generated by Django 4.1.6 on 2023-04-12 15:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tc', '0031_class_test_alter_class_code_alter_class_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='class',
            name='tc',
            field=models.ManyToManyField(to='tc.testconductor'),
        ),
        migrations.AddField(
            model_name='testconductor',
            name='classes',
            field=models.ManyToManyField(blank=True, to='tc.class'),
        ),
    ]
