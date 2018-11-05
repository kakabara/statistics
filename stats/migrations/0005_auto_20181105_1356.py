# Generated by Django 2.0.9 on 2018-11-05 13:56

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stats', '0004_auto_20181104_1333'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mileage',
            name='year',
            field=models.IntegerField(default=2000, validators=[django.core.validators.MinValueValidator(2000)]),
        ),
    ]
