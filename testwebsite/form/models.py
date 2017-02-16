from __future__ import unicode_literals

from django.db import models

from django_extensions.db.models import TimeStampedModel

# Create your models here.
class Form(TimeStampedModel):
    name = models.CharField(max_length=250, unique=True, verbose_name="Name")
    favorite_color = models.CharField(max_length=250, verbose_name="Favorite Color")
    cats_or_dogs = models.CharField(max_length=250, verbose_name="Cats or Dogs?")


class List(TimeStampedModel):
    name = models.CharField(max_length=250, unique=True, verbose_name="Name")
    favorite_color = models.CharField(max_length=250, verbose_name="Favorite Color")
    cats_or_dogs = models.CharField(max_length=250, verbose_name="Cats or Dogs?")

    def __unicode__(self):
        return u'%s' % (self.name,)
