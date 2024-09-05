#--------------------# WHAT ADMIN WILL SEE #--------------------#

from django.contrib import admin
from .models import SegEstrada

class SegEstradaAdmin(admin.ModelAdmin):
    list_display = ('id', 'long_start', 'lat_start', 'long_end', 'lat_end', 'length', 'speed', 'tempo_reg', 'views_count')

admin.site.register(SegEstrada, SegEstradaAdmin)
