# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-11-13 19:17
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('glazing', '0008_climate_zone_interior'),
    ]

    operations = [
        migrations.AddField(
            model_name='climate_zone',
            name='CSHGC',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='climate_zone',
            name='CU',
            field=models.FloatField(default=0),
        ),
    ]
