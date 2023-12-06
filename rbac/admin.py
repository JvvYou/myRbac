from django.contrib import admin
from .models import UserProfile, Permission, Organization, Role, Menu
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .forms.user import UserCreationForm, UserChangeForm
from django.contrib.auth.models import Group


class UserAdmin(BaseUserAdmin):
    list_display = ('email', 'username', 'mobile', 'image', 'department', 'position', 'superior',
                    'is_superuser', 'is_admin', 'date_joined', 'last_login')
    list_filter = ('is_superuser',)
    fieldsets = (
        ('基础信息', {'fields': ('email', 'mobile', 'username', 'image')}),
        ('Personal info', {'fields': ('department', 'position', 'superior', 'roles')}),
        ('Permissions', {'fields': ('is_admin', 'is_superuser', 'is_active',)}),
    )
    add_fieldsets = (
        ('必填', {
            'classes': ('wide',),
            'fields': ('email', 'username', 'password1', 'password2'),
        }),
    )
    form = UserChangeForm
    add_form = UserCreationForm
    search_fields = ('mobile', 'email', 'username')
    ordering = ('mobile',)
    filter_horizontal = ('roles',)  # m2m


admin.site.register(UserProfile, UserAdmin)
admin.site.unregister(Group)
admin.site.register(Permission)
admin.site.register(Organization)
admin.site.register(Role)
admin.site.register(Menu)
