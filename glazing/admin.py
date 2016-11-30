from django.contrib import admin

from .models import *

class GlassAdmin(admin.ModelAdmin):
    list_display = ('description',)
    list_filter = ('category__description',)
    search_fields = ['description']
 
admin.site.register(Glass, GlassAdmin)
admin.site.register(Frame)

class Glass_Frame_JoinAdmin(admin.ModelAdmin):
    list_display = ('glass', 'frame', 'SHGC', 'U_Value')
    list_filter = ('frame','glass__category',)
    search_fields = ['glass__description']

admin.site.register(Glass_Frame_Join,Glass_Frame_JoinAdmin)
admin.site.register(Climate_Zone)
admin.site.register(Orientation)
admin.site.register(Glazing_Project)

class WindowsAdmin(admin.ModelAdmin):
    list_display = ('width', 'height', 'ph')

admin.site.register(Windows, WindowsAdmin)
admin.site.register(Glass_Category)

class Solar_Exposure_FactorAdmin(admin.ModelAdmin):
    list_display = ('zone', 'orientation', 'ph', 'e')
    list_filter = ('zone__description','orientation__description',)

admin.site.register(Solar_Exposure_Factor, Solar_Exposure_FactorAdmin)