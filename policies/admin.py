from django.contrib import admin
from .models import PolicyBase, InsuredAccident, IFLPolicy, NSPolicy, VZRPolicy, RequestChanges, InsuredProperty


admin.site.register(PolicyBase)
admin.site.register(NSPolicy)
admin.site.register(IFLPolicy)
admin.site.register(VZRPolicy)