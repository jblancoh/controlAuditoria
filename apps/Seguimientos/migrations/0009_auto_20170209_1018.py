# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-02-09 16:18
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Seguimientos', '0008_auto_20170209_1003'),
    ]

    operations = [
        migrations.AlterField(
            model_name='seguimientos',
            name='Fechaseguimiento',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2017, 2, 9, 10, 18, 11, 283133)),
        ),
    ]
