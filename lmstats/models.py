# -*- coding: utf-8-*-
from django.db import models

# Create your models here.
# Create your models here.
class HostGroup(models.Model):
    name = models.CharField(max_length=60, unique = True)
    active = models.BooleanField()
    date_created = models.DateTimeField('date created')

    def __unicode__(self):
        return self.name

    
class Computer(models.Model):
    name = models.CharField(max_length=60)
    host_group = models.ForeignKey(HostGroup)
    active = models.BooleanField()
    date_created = models.DateTimeField('date created')


    def __unicode__(self):
        return self.name