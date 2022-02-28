from django.contrib import admin
from .models import *


@admin.register(SundayServicesVespers)
class SundayServicesVespersAdmin(admin.ModelAdmin):
    list_display = ['voice', 'gv1', 'gv2', 'gv3', 'gv4', 'gv5', 'gv6', 'gv7', 'gv8', 'gv9', 'gv10', 'dogmatic']
    list_editable = ['gv1', 'gv2', 'gv3', 'gv4', 'gv5', 'gv6', 'gv7', 'gv8', 'gv9', 'gv10', 'dogmatic']
    ordering = ['voice']


@admin.register(SundayServicesMatins)
class SundayServicesMatinsAdmin(admin.ModelAdmin):
    list_display = ['voice', 'tropar', 'bg_tr', 'sed1a', 'sed1b', 'bg_sed1', 'sed2a', 'sed2b', 'bg_sed2', 'ipac',
                    'step', 'bg_step', 'procimen', 'st_proc', 'kondac', 'icos', 'hv1', 'hv2', 'hv3', 'hv4', 'hv5',
                    'hv6', 'hv7', 'hv8']
    list_editable = ['tropar', 'bg_tr', 'sed1a', 'sed1b', 'bg_sed1', 'sed2a', 'sed2b', 'bg_sed2', 'ipac', 'step',
                     'bg_step', 'procimen', 'st_proc', 'kondac', 'icos', 'hv1', 'hv2', 'hv3', 'hv4', 'hv5', 'hv6',
                     'hv7', 'hv8']
    ordering = ['voice']


@admin.register(Canon)
class CanonAdmin(admin.ModelAdmin):
    list_display = ['voice', 'pesn1', 'pesn3', 'pesn4', 'pesn5', 'pesn6', 'pesn7', 'pesn8', 'pesn9']
    list_editable = ['pesn1', 'pesn3', 'pesn4', 'pesn5', 'pesn6', 'pesn7', 'pesn8', 'pesn9']
    ordering = ['voice']


@admin.register(SundayTropar)
class SundayTroparAdmin(admin.ModelAdmin):
    list_display = ['id', 'voices', 'text']
    ordering = ['id']


@admin.register(EvangSunday)
class EvangSundayAdmin(admin.ModelAdmin):
    list_display = ['id', 'evang', 'exapost', 'st_ev']
    list_editable = ['evang', 'exapost', 'st_ev']
    ordering = ['id']
