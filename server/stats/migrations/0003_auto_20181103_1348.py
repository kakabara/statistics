# Generated by Django 2.1.2 on 2018-11-03 06:48

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stats', '0002_auto_20181103_1341'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mileage',
            name='year',
            field=models.DateField(default=datetime.date.today),
        ),
    ]
