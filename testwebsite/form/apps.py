from __future__ import unicode_literals

from django.apps import AppConfig

from django import forms

from .models import List

class FormConfig(AppConfig):
    name = 'form'

class DetailsForm(forms.Form):
    name = forms.CharField()
    color = forms.CharField()
    cats_or_dogs = forms.CharField()

class DetailsModelForm(forms.ModelForm):
    class Meta:
        model = List
        fields = '__all__'
