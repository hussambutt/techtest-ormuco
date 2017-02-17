from __future__ import unicode_literals

from django.apps import AppConfig

from django import forms

class FormConfig(AppConfig):
    name = 'form'

class DetailsForm(forms.Form):
    name = forms.CharField()
    color = forms.CharField()
    cats_or_dogs = forms.CharField()
