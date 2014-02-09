from django.db import models
from django.utils.translation import gettext as _


class Product(models.Model):
    name = models.CharField(max_length=128)
    # The actual product's internal name, I am sure all products have one
    # This simplifies the database table function invocations
    product_code = models.CharField(max_length=128, unique=True)

    def __unicode__(self):
        return self.name


class Location(models.Model):

    class Meta:
        verbose_name = _('Location')
        verbose_name_plural = _('Locations')

    description = models.CharField(max_length=128)
    code = models.CharField(max_length=12, unique=True)

    def __unicode__(self):
        return self.description


class Source(models.Model):

    """
    Represents the concept of a data source
    Ideally this should define where the data should be obtained
    For now, we will be using filtering to get this done with
    """
    class Meta:
        verbose_name = _('Source')
        verbose_name_plural = _('Sources')

    name = models.CharField(max_length=128)
    code = models.CharField(max_length=28)

    def __unicode__(self):
        return self.name


class Indicator(models.Model):
    name = models.CharField(max_length=128, unique=True)
    description = models.CharField(max_length=128)

    # Determines the order of the field during rendering
    # In case there are multiple indicators to be displayed
    order = models.IntegerField(default=0)

    # Determines custom factors
    # Set of locations for which this indicator needs to be calculated
    locations = models.ManyToManyField(Location)
    # The product to which this is associated
    product = models.ForeignKey(Product)
    # The data source of this indicator
    source = models.ManyToManyField(Source)

    def __unicode__(self):
        return self.name
