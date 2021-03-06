# Generated by Django 3.1.5 on 2021-01-14 10:33

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0003_auto_20210114_1201'),
    ]

    operations = [
        migrations.AddField(
            model_name='forthyear',
            name='desc_en',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='forthyear',
            name='name_en',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='secondyear',
            name='desc_en',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='secondyear',
            name='name_en',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='thirdyear',
            name='desc_en',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='thirdyear',
            name='name_en',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='buyconfirmation',
            name='date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 1, 14, 12, 33, 11, 7720)),
        ),
    ]
