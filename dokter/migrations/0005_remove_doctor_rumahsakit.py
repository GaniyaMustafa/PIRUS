# Generated by Django 3.1.1 on 2020-11-09 04:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dokter', '0004_auto_20201109_1140'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='doctor',
            name='rumahsakit',
        ),
    ]
