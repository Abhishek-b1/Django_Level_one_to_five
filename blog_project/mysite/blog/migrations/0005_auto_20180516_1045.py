# -*- coding: utf-8 -*-
# Generated by Django 1.11.12 on 2018-05-16 10:45
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_auto_20180516_1045'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='create_date',
            field=models.DateTimeField(default=datetime.datetime(2018, 5, 16, 10, 45, 50, 578979, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='post',
            name='create_date',
            field=models.DateField(default=datetime.datetime(2018, 5, 16, 10, 45, 50, 578177, tzinfo=utc)),
        ),
    ]
