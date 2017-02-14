# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-02-08 17:19
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Seguimientos', '0006_auto_20170208_1110'),
    ]

    operations = [
        migrations.AlterField(
            model_name='alerta',
            name='Estatus',
            field=models.ForeignKey(default=1, null=True, on_delete=django.db.models.deletion.CASCADE, to='Catalogos.Estatus'),
        ),
        migrations.AlterField(
            model_name='seguimientos',
            name='Estatus',
            field=models.ForeignKey(default=1, null=True, on_delete=django.db.models.deletion.CASCADE, to='Catalogos.Estatus'),
        ),
        migrations.AlterField(
            model_name='seguimientos',
            name='Fechaseguimiento',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2017, 2, 8, 11, 19, 33, 125364)),
        ),
    ]
