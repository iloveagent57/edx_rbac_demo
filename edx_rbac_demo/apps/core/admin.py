""" Admin configuration for core models. """

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import ugettext_lazy as _

from edx_rbac_demo.apps.core.models import (
    Account,
    User,
    DemoFeatureRole,
    DemoRoleAssignment,
)


class DemoFeatureRoleAdmin(admin.ModelAdmin):
    pass


class DemoRoleAssignmentAdmin(admin.ModelAdmin):
    pass


class AccountAdmin(admin.ModelAdmin):
    pass


class CustomUserAdmin(UserAdmin):
    """ Admin configuration for the custom User model. """
    list_display = ('username', 'email', 'full_name', 'first_name', 'last_name', 'is_staff')
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        (_('Personal info'), {'fields': ('full_name', 'first_name', 'last_name', 'email')}),
        (_('Permissions'), {'fields': ('is_active', 'is_staff', 'is_superuser',
                                       'groups', 'user_permissions')}),
        (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
    )


admin.site.register(User, CustomUserAdmin)
admin.site.register(Account, AccountAdmin)
admin.site.register(DemoFeatureRole, DemoFeatureRoleAdmin)
admin.site.register(DemoRoleAssignment, DemoRoleAssignmentAdmin)
