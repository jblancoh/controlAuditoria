# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-14 03:51
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Seguimientos', '0025_auto_20170214_0345'),
    ]

    operations = [
        migrations.AlterField(
            model_name='seguimientos',
            name='Fechaseguimiento',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2017, 2, 14, 3, 51, 21, 419738)),
        ),
    ]
