# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-11-13 22:27
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('glazing', '0013_auto_20161113_2133'),
    ]

    operations = [
        migrations.RenameField(
            model_name='frame_products_join_tbl',
            old_name='IGDB_SHGC',
            new_name='SHGC',
        ),
        migrations.RenameField(
            model_name='frame_products_join_tbl',
            old_name='Shading_coefficient',
            new_name='U_value',
        ),
        migrations.RemoveField(
            model_name='frame',
            name='SHGC',
        ),
        migrations.RemoveField(
            model_name='frame',
            name='U',
        ),
        migrations.RemoveField(
            model_name='frame_products_join_tbl',
            name='UV_elimination',
        ),
        migrations.RemoveField(
            model_name='frame_products_join_tbl',
            name='noise_control',
        ),
        migrations.RemoveField(
            model_name='frame_products_join_tbl',
            name='primadoor_tested_SHGC',
        ),
        migrations.RemoveField(
            model_name='frame_products_join_tbl',
            name='primadoor_tested_U_value',
        ),
        migrations.RemoveField(
            model_name='frame_products_join_tbl',
            name='safety_rating',
        ),
        migrations.RemoveField(
            model_name='frame_products_join_tbl',
            name='security_rating',
        ),
        migrations.RemoveField(
            model_name='frame_products_join_tbl',
            name='solar_energy_absorption',
        ),
        migrations.RemoveField(
            model_name='frame_products_join_tbl',
            name='solar_energy_direct_transmission',
        ),
        migrations.RemoveField(
            model_name='frame_products_join_tbl',
            name='solar_energy_reflect',
        ),
        migrations.RemoveField(
            model_name='frame_products_join_tbl',
            name='solar_energy_total_elimination',
        ),
        migrations.RemoveField(
            model_name='frame_products_join_tbl',
            name='system_U_value_alum_steel',
        ),
        migrations.RemoveField(
            model_name='frame_products_join_tbl',
            name='system_U_value_timber_uPVC_alumn_thermally_broken',
        ),
        migrations.RemoveField(
            model_name='frame_products_join_tbl',
            name='visible_light_reflect',
        ),
        migrations.RemoveField(
            model_name='frame_products_join_tbl',
            name='visible_light_transmission',
        ),
        migrations.RemoveField(
            model_name='glass',
            name='product_range',
        ),
        migrations.AddField(
            model_name='glass',
            name='Shading_coefficient',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='glass',
            name='UV_elimination',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='glass',
            name='noise_control',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='glass',
            name='safety_rating',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='glass',
            name='security_rating',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='glass',
            name='solar_energy_absorption',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='glass',
            name='solar_energy_direct_transmission',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='glass',
            name='solar_energy_reflect',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='glass',
            name='solar_energy_total_elimination',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='glass',
            name='visible_light_reflect',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='glass',
            name='visible_light_transmission',
            field=models.IntegerField(default=0),
        ),
    ]
