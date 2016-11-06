#-*- coding: utf-8 -*-
from django import forms

from .models import Glazing_Project, Windows, Orientation

class GlazingProjectForm(forms.ModelForm):
  
  class Meta:
    model = Glazing_Project
    fields = ('description', 'floor_number','climate_zone_id')

class WindowsForm(forms.ModelForm):

  #orientation_id = forms.ModelChoiceField(queryset=Orientation.objects.all().order_by('description'),
   #                                       initial=0)

  class Meta:
    model = Windows
    fields = ('glazing_project_id', 'description', 'width', 'height', 'orientation_id', 'products_id')