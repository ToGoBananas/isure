from django.contrib import admin
from .models import PolicyInsured, PolicyBase, InsuredAccident, IFLPolicy, NSPolicy, VZRPolicy, RequestChanges, InsuredProperty



admin.site.register(PolicyBase)
admin.site.register(InsuredAccident)
admin.site.register(IFLPolicy)
admin.site.register(NSPolicy)
admin.site.register(VZRPolicy)
admin.site.register(RequestChanges)
admin.site.register(InsuredProperty)
admin.site.register(PolicyInsured)