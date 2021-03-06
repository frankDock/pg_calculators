# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-11-13 22:50
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('glazing', '0015_auto_20161113_2246'),
    ]

    operations = [
        migrations.CreateModel(
            name='Glass_Frame_Join',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('SHGC', models.FloatField(default=0)),
                ('U_Value', models.FloatField(default=0)),
                ('frame_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='glazing.Frame')),
                ('product_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='glazing.Glass')),
            ],
            options={
                'verbose_name': 'Frame/Glass SHGC & U-Value',
                'verbose_name_plural': 'Frame/Glass SHGC & U-Values',
            },
        ),
        migrations.RemoveField(
            model_name='shgc',
            name='frame_id',
        ),
        migrations.RemoveField(
            model_name='shgc',
            name='product_id',
        ),
        migrations.RemoveField(
            model_name='u_value',
            name='frame_id',
        ),
        migrations.RemoveField(
            model_name='u_value',
            name='product_id',
        ),
        migrations.DeleteModel(
            name='SHGC',
        ),
        migrations.DeleteModel(
            name='U_Value',
        ),
    ]
