# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-13 00:27
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('exchange', '0005_auto_20170612_0015'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Task_Historic',
        ),
    ]
