# Generated by Django 3.1.1 on 2020-11-09 04:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dokter', '0003_auto_20201109_1133'),
    ]

    operations = [
        migrations.AlterField(
            model_name='doctor',
            name='image',
            field=models.ImageField(default='static/img/doctor-icon.png', upload_to='img/dokter/'),
        ),
    ]
