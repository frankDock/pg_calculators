from django.contrib import admin

from .models import *

admin.site.register(Glass)
admin.site.register(Frame)
admin.site.register(Glass_Frame_Join)
admin.site.register(Climate_Zone)
admin.site.register(Orientation)
admin.site.register(Glazing_Project)

class WindowsAdmin(admin.ModelAdmin):
    list_display = ('width', 'height', 'ph')

admin.site.register(Windows, WindowsAdmin)
admin.site.register(Glass_Category)
admin.site.register(Solar_Exposure_Factor)