from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser


class CustomUserAdminConfig(UserAdmin):
    search_fields = ('email', 'user_name', 'first_name',)
    ordering = ("-start_date",)
    list_display = ('email', 'id', 'user_name', 'first_name', 'is_active', 'is_staff',)
    fieldsets = (
        (None, {'fields': ('email', 'user_name', 'first_name',)}),
        ('Permissions', {'fields': ('is_staff', 'is_active')}),
        ('Personal', {'fields': ('about',)}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'user_name', 'first_name', 'password1', 'password2'),
        }),
    )


admin.site.register(CustomUser, CustomUserAdminConfig)
