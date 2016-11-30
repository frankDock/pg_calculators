from __future__ import unicode_literals

from django.db import models
from django.core.exceptions import ObjectDoesNotExist

class Glass_Category(models.Model):
    description = models.CharField(max_length=200)

    def __unicode__(self):
        return u'{0}'.format(self.description)    
    
    class Meta:
        verbose_name = 'Glass Product Category'
        verbose_name_plural = 'Glass Product Categories'

class Glass(models.Model):
    description = models.CharField(max_length=200)
    category = models.ForeignKey(Glass_Category)
    visible_light_transmission = models.IntegerField(default=0)
    visible_light_reflect = models.IntegerField(default=0)
    solar_energy_total_elimination = models.IntegerField(default=0)
    solar_energy_reflect = models.IntegerField(default=0)
    solar_energy_absorption = models.IntegerField(default=0)
    solar_energy_direct_transmission = models.IntegerField(default=0)
    Shading_coefficient = models.FloatField(default=0)
    UV_elimination = models.FloatField(default=0)
    noise_control = models.IntegerField(default=0)
    safety_rating = models.IntegerField(default=0)
    security_rating = models.IntegerField(default=0)

    class Meta:
        verbose_name = 'Glass Product'
        verbose_name_plural = 'Glass Products'


    def __unicode__(self):
        return u'{0}'.format(self.description)
    
class Frame(models.Model):
    description = models.CharField(max_length=200)

    def __unicode__(self):
        return u'{0}'.format(self.description)

class Glass_Frame_Join(models.Model):
    frame = models.ForeignKey(Frame)
    glass = models.ForeignKey(Glass)
    SHGC = models.FloatField(default=0)
    U_Value = models.FloatField(default=0)

    class Meta:
        verbose_name = 'Frame/Glass SHGC & U-Value'
        verbose_name_plural = 'Frame/Glass SHGC & U-Values' 
    
class Climate_Zone(models.Model):
    description = models.CharField(max_length=200)
    interior = models.CharField(max_length=200)
    CU = models.FloatField(default=0)
    CSHGC = models.FloatField(default=0)

    class Meta:
        verbose_name = 'Climate Zone'
        verbose_name_plural = 'Climate Zones'

    def __unicode__(self):
        return u'{0} {1}'.format(self.description, self.interior)
    
class Orientation(models.Model):
    description = models.CharField(max_length=200)
    symbol = models.CharField(max_length=200)

    def __unicode__(self):
        return u'{0}'.format(self.description)

class Glazing_Project(models.Model):
    description = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    climate_zone_id = models.ForeignKey(Climate_Zone)
    floor_number = models.IntegerField(default=1)
    nett_floor_area = models.IntegerField(default=1)
    target_shgc = models.FloatField(default=0)
    target_u = models.FloatField(default=0)

    def __unicode__(self):
        return u'{0}'.format(self.description)
    
    class Meta:
        verbose_name = 'Glazing Project'
        verbose_name_plural = 'Glazing Projects'

    def save(self, force_insert=False, force_update=False):
        #target_shgc
        self.target_shgc = self.nett_floor_area * self.climate_zone_id.CSHGC
        self.target_u = self.nett_floor_area * self.climate_zone_id.CU

        super(Glazing_Project, self).save(force_insert, force_update)

class Solar_Exposure_Factor(models.Model):
    zone = models.ForeignKey(Climate_Zone)
    orientation = models.ForeignKey(Orientation)
    ph = models.FloatField(default=0)
    e = models.FloatField(default=0)

    def __unicode__(self):
        return u'{0}'.format(self.e)

    class Meta:
        verbose_name = 'Solar Exposure Factor'
        verbose_name_plural = 'Solar Exposure Factors'

class Windows(models.Model):
    glazing_project_id = models.ForeignKey(Glazing_Project, on_delete=models.CASCADE, related_name="project")
    description = models.CharField(max_length=200)
    width = models.FloatField(default=0)
    height = models.FloatField(default=0)
    shading_p = models.FloatField(default=0)
    shading_h = models.FloatField(default=0)
    orientation_id = models.ForeignKey(Orientation)
    glass_id = models.ForeignKey(Glass)
    frame_id = models.ForeignKey(Frame)
    window_area = models.FloatField(default=0)
    ph = models.FloatField(default=0)
    solar_exposure = models.ForeignKey(Solar_Exposure_Factor, null=True, blank=True, default=None)
    glass_frame_join = models.ForeignKey(Glass_Frame_Join, null=True, blank=True, default=None)
    shgc_proposed = models.FloatField(default=0)
    conductance = models.FloatField(default=0)

    class Meta:
        verbose_name = 'Window'
        verbose_name_plural = 'Windows'

    def save(self, force_insert=False, force_update=False):
        #ph
        if self.shading_h == 0:
            self.ph = 0
        else:
            if self.shading_h - self.height > 0.5:
                self.ph = (self.shading_p/2)/self.shading_h
            else:
                self.ph = self.shading_p/self.shading_h
        
        #window_area
        self.window_area = self.width * self.height

        #solar_exposure
        try:
            self.solar_exposure = Solar_Exposure_Factor.objects.get(ph = round(self.ph,1), zone = self.glazing_project_id.climate_zone_id, orientation = self.orientation_id)
        except ObjectDoesNotExist:
            self.solar_exposure = None
        
        #glass_frame_join
        try:
            self.glass_frame_join = Glass_Frame_Join.objects.get(glass = self.glass_id, frame = self.frame_id)
        except ObjectDoesNotExist:
            self.glass_frame_join = None
        
        #shgc_proposed
        try:
            self.shgc_proposed = round(self.window_area * self.solar_exposure.e * self.glass_frame_join.SHGC,2)
        except:
            self.shgc_proposed = 0
        
        #conductance
        try:
            self.conductance = round(self.window_area * self.glass_frame_join.U_Value,2)
        except:
            self.conductance = 0

        super(Windows, self).save(force_insert, force_update)
    


    