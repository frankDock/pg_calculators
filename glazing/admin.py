from .models import *
from .forms import *
from django import forms
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User

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

class AccountAdmin(admin.ModelAdmin):
    list_display = ('Name', 'Type')
    list_editable = ('Type',)

class UserProfileInline(admin.TabularInline):
    model = UserProfile
    fk_name = 'user'
    max_num = 1

class UserAdmin(BaseUserAdmin):

    inlines = [UserProfileInline,]

    list_display = ('email','username', 'is_superuser')

    fieldsets = (
        (None, {'fields': ('username', 'email')}),
    )
    # add_fieldsets is not a standard ModelAdmin attribute. UserAdmin
    # overrides get_fieldsets to use this attribute when creating a user.
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'email', 'password1', 'password2')}
        ),
    )
    search_fields = ('email',)
    ordering = ('-date_joined',)
    filter_horizontal = ()

# Now register the new UserAdmin...
admin.site.unregister(User)
admin.site.register(User, UserAdmin)

# ... and, since we're not using Django's built-in permissions,
# unregister the Group model from admin.
# admin.site.unregister(Group)
