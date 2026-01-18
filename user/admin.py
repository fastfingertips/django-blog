from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User

@admin.register(User)
class CustomUserAdmin(UserAdmin):
    model = User
    
    # Use fieldsets from UserAdmin and append personal info
    fieldsets = (UserAdmin.fieldsets or ()) + (
        ('Extra Info', {'fields': ('theme_preference', 'bio', 'profile_picture')}),
    )
    
    # add_fieldsets usually not present on UserAdmin by default in some versions or types
    add_fieldsets = getattr(UserAdmin, 'add_fieldsets', ()) + (
        ('Extra Info', {'fields': ('theme_preference', 'bio')}),
    )
    
    list_display = ['username', 'email', 'theme_preference', 'is_staff']
