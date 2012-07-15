'''
Created on Jul 15, 2012

@author: luiscberrocal
'''
from django.contrib import admin
from models import Computer, HostGroup
admin.site.register(Computer)
admin.site.register(HostGroup)