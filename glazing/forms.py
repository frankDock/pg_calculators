# -*- coding: utf-8 -*-
from django import forms
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from .models import *


class UserForm(forms.Form):
    id = models.AutoField(primary_key=True)
    username = forms.RegexField(regex=r'^\w+$', widget=forms.TextInput(attrs=dict(required=True, max_length=30)),
                                error_messages={
                                    'invalid': "This value must contain only letters, numbers and underscores."})
    email = forms.EmailField(widget=forms.TextInput(attrs=dict(required=True, max_length=30)), label="Email address")
    password1 = forms.CharField(
        widget=forms.PasswordInput(attrs=dict(required=True, max_length=30, render_value=False)), label="Password")
    password2 = forms.CharField(
        widget=forms.PasswordInput(attrs=dict(required=True, max_length=30, render_value=False)),
        label="Password (again)")

    def clean_username(self):
        try:
            user = User.objects.get(username__iexact=self.cleaned_data['username'])
        except User.DoesNotExist:
            return self.cleaned_data['username']
        raise forms.ValidationError("The username already exists. Please try another one.")

    def clean(self):
        if (self.clean.im_self['password1'].data != '') and (self.clean.im_self['password2'].data != ''):
            if self.clean.im_self['password1'].data != self.clean.im_self['password2'].data:
                return "The two password fields did not match."
        return True

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')


class ProfileForm(forms.ModelForm):
    TYPES = (('glass and aluminium fabricator', 'glass and aluminium fabricator'),
             ('contruction company', 'contruction company'),
             ('architect', 'architect'))
    company = forms.MultipleChoiceField(widget=forms.Select, choices=TYPES)

    class Meta:
        model = UserProfile
        fields = ('company', 'user',)


class EmptyChoiceField(forms.ChoiceField):
    def __init__(self, choices=(), empty_label=None, required=True, widget=None, label=None, initial=None,
                 help_text=None, *args, **kwargs):
        # prepend an empty label if it exists (and field is not required!)
        if not required and empty_label is not None:
            choices = tuple([(u'', empty_label)] + list(choices))

        super(EmptyChoiceField, self).__init__(choices=choices, required=required, widget=widget, label=label,
                                               initial=initial, help_text=help_text, *args, **kwargs)


class GlazingProjectForm(forms.ModelForm):
    class Meta:
        model = Glazing_Project
        fields = ('description', 'floor_number', 'climate_zone_id', 'nett_floor_area')


class WindowsForm(forms.ModelForm):
    class Meta:
        model = Windows

        exclude = ['ph', 'window_area', 'solar_exposure', 'glass_frame_join', 'shgc_proposed', 'conductance']

    description = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    width = forms.CharField(label='Width (m)', widget=forms.TextInput(attrs={'class': 'form-control'}))
    height = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    shading_p = forms.CharField(label='Shading P', widget=forms.TextInput(attrs={'class': 'form-control'}))
    shading_h = forms.CharField(label='Shading H', widget=forms.TextInput(attrs={'class': 'form-control'}))



