# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-11-15 10:55
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('glazing', '0019_auto_20161115_1047'),
    ]

    operations = [
        migrations.AddField(
            model_name='glazing_project',
            name='target_u',
            field=models.FloatField(default=0),
        ),
    ]
