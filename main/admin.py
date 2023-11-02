from django.contrib import admin
from .models import Manufacturer, MeterModel, Meter, PersonalAccount, InstalledMeter

admin.site.register(Manufacturer)
admin.site.register(MeterModel)
admin.site.register(Meter)
admin.site.register(PersonalAccount)
admin.site.register(InstalledMeter)
