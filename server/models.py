# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.utils.encoding import python_2_unicode_compatible
from django.db import models

# Create your models here.


@python_2_unicode_compatible
class Provider(models.Model):

    name = models.CharField(max_length=256)

    def __str__(self):
        return self.name


@python_2_unicode_compatible
class OperationSystem(models.Model):

    name = models.CharField(max_length=256)

    def __str__(self):
        return self.name


@python_2_unicode_compatible
class HardDisk(models.Model):
    TYPE = (('ssd', 'SSD'),
            ('hd', 'HD'),)

    hd_type = models.CharField(verbose_name=u'Type', max_length=4,
                               choices=TYPE)
    amount_of_hd = models.FloatField(verbose_name=u'Hd (GB)')

    def __str__(self):
        return "%(amount)s %(hd_type)s" % {'amount': self.amount_of_hd,
                                           'hd_type': self.hd_type}


@python_2_unicode_compatible
class Instance(models.Model):

    name = models.CharField(max_length=256)
    system = models.ForeignKey('OperationSystem')
    amount_of_cpu = models.PositiveSmallIntegerField(default=1,
                                                     verbose_name=u'CPUs')
    amount_of_memory = models.FloatField(verbose_name=u'Memory (GB)')
    hd = models.ForeignKey('HardDisk')
    provider = models.ForeignKey('Provider')
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.name
