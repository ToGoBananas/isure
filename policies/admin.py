from django.contrib import admin
from .models import PolicyBase, InsuredAccident, IFLPolicy, NSPolicy, VZRPolicy


admin.site.register(PolicyBase)
admin.site.register(InsuredAccident)
admin.site.register(IFLPolicy)
admin.site.register(NSPolicy)
admin.site.register(VZRPolicy)
