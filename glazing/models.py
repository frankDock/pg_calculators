from __future__ import unicode_literals

from django.db import models

class Products(models.Model):
    description = models.CharField(max_length=200)
    category = models.IntegerField(default=1)
    product_range = models.IntegerField(default=1)
    
class Frame(models.Model):
    description = models.CharField(max_length=200)

class Frame_Products_Join_Tbl(models.Model):
    frame_id = models.ForeignKey(Frame)
    product_id = models.ForeignKey(Products)
    visible_light_transmission = models.IntegerField(default=0)
    visible_light_reflect = models.IntegerField(default=0)
    solar_energy_total_elimination = models.IntegerField(default=0)
    solar_energy_reflect = models.IntegerField(default=0)
    solar_energy_absorption = models.IntegerField(default=0)
    solar_energy_direct_transmission = models.IntegerField(default=0)
    IGDB_SHGC = models.FloatField(default=0)
    system_U_value_alum_steel = models.FloatField(default=0)
    system_U_value_timber_uPVC_alumn_thermally_broken = models.FloatField(default=0)
    primadoor_tested_SHGC = models.FloatField(default=0)
    primadoor_tested_U_value = models.FloatField(default=0)
    Shading_coefficient = models.FloatField(default=0)
    UV_elimination = models.FloatField(default=0)
    noise_control = models.IntegerField(default=0)
    safety_rating = models.IntegerField(default=0)
    security_rating = models.IntegerField(default=0)

class Climate_Zone(models.Model):
    description = models.CharField(max_length=200)
    
class Orientation(models.Model):
    description = models.CharField(max_length=200)

class Glazing_Project(models.Model):
    description = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    climate_zone_id = models.ForeignKey(Climate_Zone)
    floor_number = models.IntegerField(default=1)
    nett_floor_area = models.IntegerField(default=1)
    conductance_constant = models.FloatField(default=0)
    CSHGC = models.FloatField(default=0)

class Windows(models.Model):
    glazing_project_id = models.ForeignKey(Glazing_Project, on_delete=models.CASCADE)
    description = models.CharField(max_length=200)
    width = models.FloatField(default=0)
    height = models.FloatField(default=0)
    shading_p = models.FloatField(default=0)
    shading_h = models.FloatField(default=0)
    orientation_id = models.ForeignKey(Orientation)
    products_id = models.ForeignKey(Products)
    window_area = models.FloatField(default=0)
    ph = models.FloatField(default=0)
    solar_exposure = models.FloatField(default=0)
    shgc_glazing = models.FloatField(default=0)
    shgc_proposed = models.FloatField(default=0)
    u_value = models.FloatField(default=0)
    conductance = models.FloatField(default=0)
    