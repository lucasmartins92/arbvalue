# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2017-06-10 00:16
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('exchange', '0002_auto_20170605_0310'),
    ]

    operations = [
        migrations.CreateModel(
            name='order_book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('unix', models.DecimalField(decimal_places=10, max_digits=30)),
                ('type', models.CharField(max_length=3)),
                ('volume', models.DecimalField(decimal_places=10, max_digits=30)),
                ('price', models.DecimalField(decimal_places=10, max_digits=30)),
                ('exchange_pair', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='exchange.Exchange_Pair')),
            ],
        ),
    ]
