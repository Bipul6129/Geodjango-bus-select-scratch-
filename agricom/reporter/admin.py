from leaflet.admin import LeafletGeoAdmin
from django.contrib import admin
from .models import Incidences,Bus
# Register your models here.

# class IncidencesAdmin(admin.ModelAdmin):
#     list_display = ('name','location')

class IncidencesAdmin(LeafletGeoAdmin):
    list_display = ('name','location')

class BusAdmin(LeafletGeoAdmin):
    list_display = ('location','yatayat')

admin.site.register(Incidences,IncidencesAdmin)
admin.site.register(Bus,BusAdmin)
