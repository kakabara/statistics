# Generated by Django 2.1.2 on 2018-11-03 06:41

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stats', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mileage',
            name='year',
            field=models.DateField(default=datetime.date(2018, 11, 3)),
        ),
    ]
