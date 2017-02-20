from __future__ import unicode_literals

from django.db import models

from django_extensions.db.models import TimeStampedModel

# # Create your models here.
# class Form(TimeStampedModel):
#    name = models.CharField(max_length=250, unique=True, verbose_name="Name")
#    favorite_color = models.CharField(max_length=250, verbose_name="Favorite Color")
#    cats_or_dogs = models.CharField(max_length=250, verbose_name="Cats or Dogs?")

class List(TimeStampedModel):
    name = models.CharField(max_length=250, verbose_name="Name", unique=True)
    favorite_color = models.CharField(max_length=250, verbose_name="Favorite Color")
    #cats_or_dogs = models.CharField(max_length=250, verbose_name="Cats or Dogs?")

    CAT = 'CAT'
    DOG = 'DOG'
    CATS_OR_DOGS = (
        (CAT, 'Cats'),
        (DOG, 'Dogs'),
    )
    cats_or_dogs = models.CharField(
        max_length=4,
        choices=CATS_OR_DOGS,
        default=CAT,
    )

    def __unicode__(self):
        return u'%s' % (self.name,)
