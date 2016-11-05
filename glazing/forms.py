#-*- coding: utf-8 -*-
from django import forms

from .models import Glazing_Project

class GlazingProjectForm(forms.ModelForm):
  
  class Meta:
    model = Glazing_Project
    fields = ('description', 'floor_number',)