# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2017-06-12 03:15
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exchange', '0004_task_historic'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task_historic',
            name='value',
            field=models.CharField(max_length=80),
        ),
    ]
