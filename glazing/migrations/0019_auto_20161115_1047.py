# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-11-15 10:47
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('glazing', '0018_auto_20161113_2317'),
    ]

    operations = [
        migrations.AddField(
            model_name='glazing_project',
            name='target_shgc',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='windows',
            name='glazing_project_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='project', to='glazing.Glazing_Project'),
        ),
    ]