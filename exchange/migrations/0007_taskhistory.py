# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-13 00:37
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exchange', '0006_delete_task_historic'),
    ]

    operations = [
        migrations.CreateModel(
            name='TaskHistory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('unix', models.DecimalField(decimal_places=10, max_digits=30)),
            ],
        ),
    ]