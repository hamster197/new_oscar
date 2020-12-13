from oscar.apps.shipping.admin import *  # noqa

from django.contrib import admin

from apps.shipping.models import StandardMethod

class StandardMethodAdmin(admin.ModelAdmin):
    list_display = ('name',)
admin.site.register(StandardMethod, StandardMethodAdmin)

from oscar.apps.shipping.admin import *  # noqa
admin.site.unregister(OrderAndItemCharges)
admin.site.unregister(WeightBased)