#-*- coding: utf-8 -*-
from django import forms

from .models import *

class EmptyChoiceField(forms.ChoiceField):
    	def __init__(self, choices=(), empty_label=None, required=True, widget=None, label=None, initial=None, help_text=None, *args, **kwargs):

		# prepend an empty label if it exists (and field is not required!)
		if not required and empty_label is not None:
			choices = tuple([(u'', empty_label)] + list(choices))

		super(EmptyChoiceField, self).__init__(choices=choices, required=required, widget=widget, label=label, initial=initial, help_text=help_text, *args, **kwargs) 


class GlazingProjectForm(forms.ModelForm):
  
  class Meta:
    model = Glazing_Project
    fields = ('description', 'floor_number','climate_zone_id','nett_floor_area')

class WindowsForm(forms.ModelForm):

  
  class Meta:
    model = Windows
 
    exclude = ['ph', 'window_area', 'solar_exposure', 'glass_frame_join', 'shgc_proposed','conductance']

  description = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
  width = forms.CharField(label = 'Width (m)', widget=forms.TextInput(attrs={'class':'form-control'}))
  height = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
  shading_p = forms.CharField(label = 'Shading P', widget=forms.TextInput(attrs={'class':'form-control'}))
  shading_h = forms.CharField(label = 'Shading H', widget=forms.TextInput(attrs={'class':'form-control'}))


  
