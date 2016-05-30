from django.contrib import admin
from .models import PolicyInsured, PolicyBase, InsuredAccident, IFLPolicy, NSPolicy, VZRPolicy, RequestChanges, InsuredProperty


admin.site.register(PolicyBase)
admin.site.register(NSPolicy)