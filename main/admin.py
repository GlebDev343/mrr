from django.contrib import admin
from .models import Manufacturer, MeterModel, Meter

admin.site.register(Manufacturer)
admin.site.register(MeterModel)
admin.site.register(Meter)
