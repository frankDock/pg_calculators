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

  #orientation_id = forms.ModelChoiceField(queryset=Orientation.objects.all().order_by('description'),
   #                                       initial=0)
  
  class Meta:
    model = Windows
    fields = ('glazing_project_id', 'description', 'width', 'height', 'shading_p', 'shading_h', 'orientation_id', 'glass_id', 'frame_id')
  
  '''
  glazing_project_id = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
  description = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
  width = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
  height = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
  orientation_id = forms.IntegerField(widget=forms.Select(
    choices=Orientation.objects.all().values_list('id', 'description')))  
  products_id = forms.IntegerField(widget=forms.Select(
    choices=Products.objects.all().values_list('id', 'description')))
  '''