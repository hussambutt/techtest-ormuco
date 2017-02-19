from __future__ import unicode_literals

from django.apps import AppConfig

from django import forms

from django.utils.translation import ugettext_lazy as _

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
        # labels = {
        #     'name': _('Writer'),
        # }
        # help_texts = {
        #     'name': _('Some useful help text.'),
        # }
        error_messages = {
            'name': {
                'unique': _("Name already exists in our database."),
            },
        }