# Generated by Django 3.1.5 on 2021-01-13 15:27

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='buyconfirmation',
            name='date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 1, 13, 17, 27, 19, 679555)),
        ),
    ]
