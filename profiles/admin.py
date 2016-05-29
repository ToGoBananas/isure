from django.contrib import admin
from .models import Profile, AdditionalProfile, CustomUser
from .forms import CustomUserChangeForm, CustomUserCreationForm
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import ugettext_lazy as _
from django.conf import settings


class CustomUserAdmin(UserAdmin):
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        (_('Permissions'), {'fields': ('is_active', 'is_staff', 'is_superuser',
                                       'groups', 'user_permissions')}),
        (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2')}
        ),
    )
    form = CustomUserChangeForm
    add_form = CustomUserCreationForm
    list_display = ('email', 'is_staff')
    search_fields = ('email', )
    ordering = ('email',)


admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(AdditionalProfile)
admin.site.register(Profile)
