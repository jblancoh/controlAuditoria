# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-02-09 16:45
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Dependencia',
            fields=[
                ('idDependencia', models.AutoField(primary_key=True, serialize=False)),
                ('Dependencia', models.CharField(max_length=100, null=True)),
                ('Siglas', models.CharField(max_length=100, null=True)),
                ('Bloqueado', models.IntegerField(blank=True, default=0, editable=False)),
                ('Eliminado', models.IntegerField(blank=True, default=0, editable=False)),
            ],
        ),
    ]
