from django.contrib.auth.admin import UserAdmin
from django.contrib import admin
from django.forms import Textarea
from .models import CustomUser


class UserAdminConfig(UserAdmin):
    model = CustomUser
    search_fields = ('email', 'username', 'first_name')
    list_display = ('email', 'username', 'first_name', 'is_active', 'is_staff')
    list_filter = ('is_active', 'is_staff', 'start_date',)
    ordering = ('-start_date',)
    readonly_fields = ('start_date',)
    fieldsets = (
        (None, {'fields': ('email', 'username', 'first_name')}),
        ('Permissions', {'fields': ('is_staff', 'is_active')}),
        ('Personal', {'fields': ('start_date', 'about')})
    )
    formfield_overrides = {
        CustomUser.about: {'widget': Textarea(attrs={'rows': 10, 'cols': 40})}
    }
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'username', 'first_name', 'password1', 'password2', 'is_staff', 'is_active')
        }),
    )


admin.site.register(CustomUser, UserAdminConfig)
