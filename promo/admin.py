from django.contrib import admin
from .models import PromoProfile


class PromoProfileAdmin(admin.ModelAdmin):
    readonly_fields = ('personal_code', )


admin.site.register(PromoProfile, PromoProfileAdmin)