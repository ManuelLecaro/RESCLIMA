from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(Sensor)
admin.site.register(Variable)
admin.site.register(SensorVariable)
admin.site.register(Measurement)
